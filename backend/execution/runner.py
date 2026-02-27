import ast
import re
import sys
import os
import time
import tempfile
import subprocess
import traceback
import threading
from typing import List, Tuple, Optional
import asyncio
from fastapi import WebSocket, WebSocketDisconnect

# Modules that are ALWAYS forbidden (security)
ALWAYS_FORBIDDEN = {
    # System modules are now permitted as we are isolated in Docker!
    "socket", "multiprocessing", "threading",
    "asyncio", "pty", "tty", "termios", "signal", "resource",
    "gc", "weakref", "inspect", "traceback", "linecache",
    "tokenize", "pickle", "shelve", "marshal",
}

# Modules that can be whitelisted per-exercise
SAFE_MODULES = {
    "math", "random", "string", "re", "json", "csv", "io",
    "datetime", "time", "collections", "itertools", "functools",
    "typing", "dataclasses", "enum", "abc", "copy", "pprint",
    "hashlib", "base64", "struct", "textwrap", "decimal",
    "fractions", "statistics", "operator",
    # Level 7 onwards
    "requests", "urllib", "http",
    # Level 8 onwards
    "argparse", "configparser",
    # Level 9 onwards
    "concurrent", "queue",
}


def check_ast_security(code: str, allowed_imports: List[str]) -> Tuple[bool, str]:
    """
    Parse code with AST and validate:
    1. No forbidden imports
    2. No dangerous builtins (exec, eval, __import__, open without allowlist)
    3. Required allowed_imports whitelist enforced
    Returns (is_safe, error_message)
    """
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return False, f"SyntaxError: {e}"

    allowed_set = set(allowed_imports)

    for node in ast.walk(tree):
        # Check import statements
        if isinstance(node, ast.Import):
            for alias in node.names:
                module_root = alias.name.split(".")[0]
                if module_root in ALWAYS_FORBIDDEN and module_root not in allowed_set:
                    return False, f"Import '{alias.name}' is not allowed in this exercise."
                if module_root not in SAFE_MODULES and module_root not in allowed_set:
                    return False, f"Import '{alias.name}' is not permitted. Allowed: {allowed_set or 'none'}"

        elif isinstance(node, ast.ImportFrom):
            module_root = (node.module or "").split(".")[0]
            if module_root in ALWAYS_FORBIDDEN and module_root not in allowed_set:
                return False, f"Import 'from {node.module}' is not allowed in this exercise."
            if module_root not in SAFE_MODULES and module_root not in allowed_set:
                return False, f"Import 'from {node.module}' is not permitted. Allowed: {allowed_set or 'none'}"

        # Check dangerous calls
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                if node.func.id in ("exec", "eval", "__import__", "compile"):
                    return False, f"Use of '{node.func.id}' is not allowed."
            elif isinstance(node.func, ast.Attribute):
                if node.func.attr in ("system", "popen", "exec_command"):
                    return False, f"Call to '{node.func.attr}' is not allowed."

    return True, ""


def run_code_safely(
    code: str,
    input_data: str,
    allowed_imports: List[str],
    timeout_secs: int = 5,
    max_output_bytes: int = 10240,
) -> dict:
    """
    Run Python code in a sandboxed subprocess.
    Returns dict with: stdout, stderr, exec_time_ms, error, timed_out
    """
    # Step 1: AST security check
    is_safe, ast_error = check_ast_security(code, allowed_imports)
    if not is_safe:
        return {
            "stdout": "",
            "stderr": ast_error,
            "exec_time_ms": 0,
            "error": ast_error,
            "timed_out": False,
        }

    # Step 2: Strip input() prompts automatically for the grader
    try:
        tree = ast.parse(code)
        
        class RemoveInputPrompts(ast.NodeTransformer):
            def visit_Call(self, node):
                self.generic_visit(node)
                if isinstance(node.func, ast.Name) and node.func.id == 'input':
                    node.args = []
                    node.keywords = []
                return node
        
        tree = RemoveInputPrompts().visit(tree)
        ast.fix_missing_locations(tree)
        code = ast.unparse(tree)
    except Exception:
        pass  # If AST manipulation fails, fall back to executing original code

    # Step 3: Write code to temp file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False, encoding="utf-8") as f:
        f.write(code)
        tmp_path = f.name

    try:
        start = time.perf_counter()
        
        abs_tmp_path = os.path.abspath(tmp_path)
        docker_cmd = [
            "docker", "run", "--rm", "-i",
            "--network=none",
            "--cpus=0.5",
            "--memory=128m",
            "-v", f"{abs_tmp_path}:/app/script.py:ro",
            "python:3.11-slim",
            "python", "-u", "/app/script.py"
        ]
        
        result = subprocess.run(
            docker_cmd,
            input=input_data.encode("utf-8") if input_data else b"",
            capture_output=True,
            timeout=timeout_secs,
            env=os.environ.copy()
        )
        elapsed = (time.perf_counter() - start) * 1000

        stdout = result.stdout.decode("utf-8", errors="replace")[:max_output_bytes]
        stderr = result.stderr.decode("utf-8", errors="replace")[:2048]

        return {
            "stdout": stdout,
            "stderr": stderr,
            "exec_time_ms": round(elapsed, 2),
            "error": stderr if result.returncode != 0 else "",
            "timed_out": False,
        }
    except subprocess.TimeoutExpired:
        return {
            "stdout": "",
            "stderr": f"Execution timed out after {timeout_secs} seconds.",
            "exec_time_ms": timeout_secs * 1000,
            "error": "TIMEOUT",
            "timed_out": True,
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": str(e),
            "exec_time_ms": 0,
            "error": str(e),
            "timed_out": False,
        }
    finally:
        try:
            os.unlink(tmp_path)
        except Exception:
            pass


# ──────────────────────────────────────────────────────────────────────────────
# Public interface expected by submissions.py
# ──────────────────────────────────────────────────────────────────────────────

class RunResult:
    """Structured result from code execution."""
    def __init__(self, stdout: str, stderr: str, execution_time_ms: float, timed_out: bool, error: str):
        self.stdout = stdout.rstrip("\n")
        self.stderr = stderr
        self.execution_time_ms = execution_time_ms
        self.timed_out = timed_out
        self.error = error


def run_code(
    code: str,
    input_data: str,
    allowed_imports: List[str],
    timeout_secs: int = 5,
) -> RunResult:
    """Public wrapper used by routers."""
    raw = run_code_safely(code, input_data, allowed_imports, timeout_secs)
    return RunResult(
        stdout=raw["stdout"],
        stderr=raw["stderr"],
        execution_time_ms=raw["exec_time_ms"],
        timed_out=raw["timed_out"],
        error=raw["error"],
    )


def validate_output(actual: str, expected: str, mode: str) -> Tuple[bool, str]:
    """Compare actual vs expected output based on comparison mode."""
    actual = actual.strip()
    expected = expected.strip()

    if mode == "exact":
        passed = actual == expected
        feedback = f"Expected:\n{expected}\n\nGot:\n{actual}" if not passed else ""
        return passed, feedback

    elif mode == "contains":
        passed = expected in actual
        feedback = f"Output should contain: {expected}" if not passed else ""
        return passed, feedback

    elif mode == "json":
        import json
        try:
            actual_obj = json.loads(actual)
            expected_obj = json.loads(expected)
            passed = actual_obj == expected_obj
            feedback = f"JSON mismatch. Expected {expected_obj}, got {actual_obj}" if not passed else ""
            return passed, feedback
        except json.JSONDecodeError:
            return False, "Output is not valid JSON."

    elif mode == "regex":
        import re
        passed = bool(re.search(expected, actual))
        feedback = f"Output did not match pattern: {expected}" if not passed else ""
        return passed, feedback

    elif mode == "contains_result":
        # For benchmark-style tests — just check if first line number matches
        actual_lines = actual.splitlines()
        expected_lines = expected.splitlines()
        if not actual_lines or not expected_lines:
            return False, "Empty output."
        passed = actual_lines[0] == expected_lines[0]
        feedback = f"Expected first line: {expected_lines[0]}, got: {actual_lines[0]}" if not passed else ""
        return passed, feedback

    # Fallback to exact
    passed = actual == expected
    return passed, f"Expected: {expected}\nGot: {actual}" if not passed else ""

async def run_code_interactive_async(
    code: str,
    allowed_imports: List[str],
    websocket: WebSocket,
    timeout_secs: int = 60,
):
    """Run code and stream IO interactively over a WebSocket."""
    is_safe, ast_error = check_ast_security(code, allowed_imports)
    if not is_safe:
        await websocket.send_json({"type": "stderr", "data": f"Security Error: {ast_error}\n"})
        await websocket.send_json({"type": "exit", "code": 1})
        return

    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False, encoding="utf-8") as f:
        f.write(code)
        tmp_path = f.name

    env = os.environ.copy()
    env["PYTHONPATH"] = ""
    env["PYTHONUNBUFFERED"] = "1"

    try:
        # Resolve absolute path for Docker volume mounting. Windows needs special handling for Docker paths sometimes,
        # but standard absolute paths usually work in modern Docker Desktop.
        abs_tmp_path = os.path.abspath(tmp_path)
        
        # Convert Windows path to Docker-compatible format if necessary (C:\ -> /c/)
        # Using standard C:\path format is usually supported by Docker Desktop on Windows natively now.
        
        # We need -i to keep stdin open, but NOT -t (TTY), as TTY messes up raw stdout parsing
        docker_cmd = [
            "docker", "run", "--rm", "-i",
            "--network=none",
            "--cpus=0.5",
            "--memory=128m",
            "-v", f"{abs_tmp_path}:/app/script.py:ro",
            "python:3.11-slim",
            "python", "-u", "/app/script.py" # -u forces unbuffered output
        ]

        process = subprocess.Popen(
            docker_cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env
        )

        loop = asyncio.get_running_loop()

        def stream_reader(stream, is_error: bool):
            try:
                while True:
                    # Use read1 to read whatever bytes are available up to 1024,
                    # without blocking to wait for the full 1024 bytes to arrive!
                    # This ensures small prompts like 'a: ' instantly flush to UI.
                    chunk = stream.read1(1024) if hasattr(stream, 'read1') else stream.read(1024)
                    if not chunk:
                        break
                    text = chunk.decode("utf-8", errors="replace")
                    msg_type = "stderr" if is_error else "stdout"
                    asyncio.run_coroutine_threadsafe(
                        websocket.send_json({"type": msg_type, "data": text}), loop
                    )
            except Exception:
                pass

        # Start background threads to read stdout/stderr from subprocess
        threading.Thread(target=stream_reader, args=(process.stdout, False), daemon=True).start()
        threading.Thread(target=stream_reader, args=(process.stderr, True), daemon=True).start()

        async def write_loop():
            try:
                while True:
                    data = await websocket.receive_text()
                    if data and process.poll() is None:
                        process.stdin.write(data.encode('utf-8'))
                        process.stdin.flush()
            except WebSocketDisconnect:
                pass
            except Exception:
                pass

        async def wait_process():
            while process.poll() is None:
                await asyncio.sleep(0.1)
            return process.returncode

        async def timeout_task():
            await asyncio.sleep(timeout_secs)
            if process.poll() is None:
                process.kill()
                try:
                    await websocket.send_json({"type": "stderr", "data": f"\n\n[Process killed after {timeout_secs}s timeout]"})
                except Exception:
                    pass

        task_write = asyncio.create_task(write_loop())
        task_timeout = asyncio.create_task(timeout_task())
        task_wait = asyncio.create_task(wait_process())

        # Wait until the process exits OR the websocket disconnects (write_loop ends)
        await asyncio.wait([task_wait, task_write], return_when=asyncio.FIRST_COMPLETED)

        if process.poll() is None:
            process.kill()

        # Clean up tasks
        task_timeout.cancel()
        task_write.cancel()
        task_wait.cancel()
        
        try:
            await websocket.send_json({"type": "exit", "code": process.returncode or 0})
        except Exception:
            pass

    except Exception as e:
        err_msg = traceback.format_exc()
        try:
            await websocket.send_json({"type": "stderr", "data": f"Internal Error: {err_msg}\n"})
            await websocket.send_json({"type": "exit", "code": 1})
        except Exception:
            pass
    finally:
        try:
            os.unlink(tmp_path)
        except Exception:
            pass
