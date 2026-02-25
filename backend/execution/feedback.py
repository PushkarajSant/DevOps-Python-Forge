"""
Failure Feedback Engine — analyzes code and errors to give helpful,
non-spoiler feedback after failed submissions.
"""
import re
from typing import Optional


def analyze_failure(
    code: str,
    stdout: str,
    stderr: str,
    expected: str,
    timed_out: bool,
) -> str:
    """Return a helpful feedback message based on failure patterns."""

    if timed_out:
        return _timeout_feedback(code)

    if stderr:
        return _stderr_feedback(stderr, code)

    # Output was produced but doesn't match
    if stdout and expected:
        return _output_mismatch_feedback(stdout, expected, code)

    if not stdout and expected:
        return "Your program produced no output. Make sure you're using print() to display results."

    return "Incorrect output. Review the problem statement and try again."


# ──────────────────────────────────────────────────────────────────────────────
# Timeout analysis
# ──────────────────────────────────────────────────────────────────────────────

def _timeout_feedback(code: str) -> str:
    hints = ["⏱️ Execution timed out."]

    if "while" in code and not re.search(r"break\b", code):
        hints.append("Your while loop may never terminate — check your loop condition or add a break.")
    elif "while True" in code:
        hints.append("You have 'while True' — make sure there's a reachable break statement.")
    elif re.search(r"for .+ in .+:", code):
        hints.append("Your loop may be iterating over a very large range. Try to reduce iterations.")
    else:
        hints.append("Check for infinite loops or recursion without a base case.")

    if re.search(r"def \w+\(.*\).*:\s*\n.*\1\(", code, re.DOTALL):
        hints.append("Possible infinite recursion detected — verify your base case.")

    return " ".join(hints)


# ──────────────────────────────────────────────────────────────────────────────
# Stderr / Exception analysis
# ──────────────────────────────────────────────────────────────────────────────

_ERROR_PATTERNS = [
    (r"NameError: name '(\w+)' is not defined",
     lambda m: f"Variable '{m.group(1)}' is not defined. Check for typos or make sure you've declared it before use."),
    (r"TypeError: (.+)",
     lambda m: f"Type error: {m.group(1)}. You might be mixing incompatible types (e.g., string + int)."),
    (r"IndexError: (.+)",
     lambda m: f"Index out of range: {m.group(1)}. Check that your list/string has enough elements."),
    (r"KeyError: (.+)",
     lambda m: f"Key {m.group(1)} not found in dictionary. Use .get() or check if key exists first."),
    (r"ValueError: (.+)",
     lambda m: f"Value error: {m.group(1)}. Check your input conversion (e.g., int() on non-numeric)."),
    (r"ZeroDivisionError",
     lambda m: "Division by zero! Add a check before dividing."),
    (r"SyntaxError: (.+)",
     lambda m: f"Syntax error: {m.group(1)}. Check for missing colons, brackets, or indentation."),
    (r"IndentationError: (.+)",
     lambda m: f"Indentation error: {m.group(1)}. Python is sensitive to whitespace — use consistent indentation."),
    (r"AttributeError: '(\w+)' object has no attribute '(\w+)'",
     lambda m: f"'{m.group(1)}' has no attribute '{m.group(2)}'. Check the available methods for this type."),
    (r"ModuleNotFoundError: No module named '(\w+)'",
     lambda m: f"Module '{m.group(1)}' is not available. Check the allowed imports for this exercise."),
    (r"ImportError: (.+)",
     lambda m: f"Import error: {m.group(1)}. Only use the imports listed in 'Allowed imports'."),
    (r"RecursionError",
     lambda m: "Maximum recursion depth exceeded. Your recursive function needs a proper base case."),
    (r"FileNotFoundError",
     lambda m: "File not found. This exercise uses stdin — read from input() instead of opening files."),
]


def _stderr_feedback(stderr: str, code: str) -> str:
    for pattern, formatter in _ERROR_PATTERNS:
        match = re.search(pattern, stderr)
        if match:
            return formatter(match)

    # Generic stderr fallback
    lines = stderr.strip().splitlines()
    last_line = lines[-1] if lines else stderr
    return f"Runtime error: {last_line}"


# ──────────────────────────────────────────────────────────────────────────────
# Output mismatch analysis
# ──────────────────────────────────────────────────────────────────────────────

def _output_mismatch_feedback(actual: str, expected: str, code: str) -> str:
    actual_s = actual.strip()
    expected_s = expected.strip()

    # Trailing whitespace / newline differences
    if actual_s == expected_s:
        return "Your output is correct but has extra whitespace or newlines. Use print() without extra spaces."

    # Case difference
    if actual_s.lower() == expected_s.lower():
        return "Output is correct but the case doesn't match. Check uppercase/lowercase characters."

    # Extra/missing quotes
    if actual_s.strip("'\"") == expected_s.strip("'\""):
        return "Your output includes extra quotes. Use print(value) not print(repr(value))."

    # Close numeric values
    try:
        a, e = float(actual_s), float(expected_s)
        if abs(a - e) < 0.01:
            return f"Close! Your answer {a} is very near the expected {e}. Check rounding."
    except ValueError:
        pass

    # Line count difference
    actual_lines = actual_s.splitlines()
    expected_lines = expected_s.splitlines()
    if len(actual_lines) != len(expected_lines):
        return f"Expected {len(expected_lines)} line(s) of output but got {len(actual_lines)}. Check your print statements."

    # Partial match — find first differing line
    for i, (a_line, e_line) in enumerate(zip(actual_lines, expected_lines)):
        if a_line != e_line:
            return f"Line {i + 1} differs. Expected '{e_line[:40]}...' but got '{a_line[:40]}...'."

    return "Output doesn't match expected. Review the expected format carefully."
