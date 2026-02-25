"""Level 8: CLI Tools — 20 exercises"""
"""Level 9: Concurrency — 15 exercises"""
"""Level 10: Capstone Projects — 5 capstones"""

# ──────────────────────────────────────────────
# Level 8: CLI Tools & Packaging
# ──────────────────────────────────────────────

def make_placeholders(level_name, topic, count, start=1, difficulty="medium", xp=20):
    return [
        {"title": f"{level_name} Exercise {i}",
         "problem_statement": f"Advanced {topic} exercise {i}. Build CLI-style tooling using Python.",
         "scenario": f"Real-world {topic} automation scenario.",
         "input_description": "Arguments passed as input lines.",
         "expected_output_description": "Processed CLI output.",
         "starter_code": "import sys\nargs = sys.stdin.read().split()\nprint(' '.join(args))\n",
         "tags": [topic.lower().replace(" ", "-")],
         "difficulty": difficulty, "xp_reward": xp, "allowed_imports": ["sys"], "timeout_secs": 5,
         "test_cases": [{"input_data": f"arg{i}", "expected_output": f"arg{i}", "is_hidden": False, "comparison_mode": "exact"}],
         "hints": [{"order_num": 1, "content": f"Think about {topic} patterns.", "unlock_after_attempts": 1}],
         "concepts": [{"title": f"{topic} concept", "explanation": f"Core {topic} concepts for DevOps CLI tools.", "code_example": "import sys\nargs = sys.argv[1:]", "unlocks_after_failures": 3}],
        } for i in range(start, start + count)
    ]

LEVEL_8_EXERCISES = [
    {
        "title": "Argument Parser Simulator",
        "problem_statement": "Read a command-line string from stdin (space-separated). Parse flags:\n--env <name>: print 'Environment: name'\n--port <n>: print 'Port: n'\n--debug: print 'Debug mode: ON'\nUnknown flags: print 'Unknown flag: --flag'",
        "scenario": "CLI tools built with argparse follow this exact pattern — parse flags and dispatch actions.",
        "input_description": "A command string like: --env prod --port 8080 --debug",
        "expected_output_description": "Environment: prod\nPort: 8080\nDebug mode: ON",
        "starter_code": "import sys\nargs = sys.stdin.read().split()\n# Parse flags: --env, --port, --debug\n",
        "tags": ["cli", "argparse", "parsing"],
        "difficulty": "hard", "xp_reward": 25, "allowed_imports": ["sys"], "timeout_secs": 5,
        "test_cases": [
            {"input_data": "--env prod --port 8080 --debug", "expected_output": "Environment: prod\nPort: 8080\nDebug mode: ON", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "--port 443", "expected_output": "Port: 443", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "--unknown", "expected_output": "Unknown flag: --unknown", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Iterate args with index. If arg is '--env', next token is the value (i+1).", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Use a while loop with index: i=0; while i < len(args): check args[i]; i++", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "Manual CLI argument parsing", "explanation": "Before argparse: iterate args, check for flags, consume the next token as the value. This is exactly what argparse does under the hood.", "code_example": "i = 0\nwhile i < len(args):\n    if args[i] == '--env':\n        print(f'Environment: {args[i+1]}')\n        i += 2\n    elif args[i] == '--debug':\n        print('Debug mode: ON')\n        i += 1", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Log Analyzer CLI Mode",
        "problem_statement": "Read a command mode (first line) and log lines. Mode can be:\n'count-errors': count ERROR lines\n'list-warnings': print WARNING lines\n'summary': print 'Total: N, Errors: E, Warnings: W'",
        "scenario": "A multi-mode log analyzer tool — one script, multiple operations triggered by a command argument.",
        "input_description": "First line: mode. Then N log lines.",
        "expected_output_description": "Mode-specific output.",
        "starter_code": "import sys\nlines = sys.stdin.read().splitlines()\nmode = lines[0]\nlog_lines = lines[1:]\n# Dispatch based on mode\n",
        "tags": ["cli", "dispatching", "logs"],
        "difficulty": "medium", "xp_reward": 20, "allowed_imports": ["sys"], "timeout_secs": 5,
        "test_cases": [
            {"input_data": "count-errors\nINFO start\nERROR fail\nWARNING high-mem\nERROR crash", "expected_output": "2", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "list-warnings\nINFO ok\nWARNING disk\nERROR db\nWARNING memory", "expected_output": "WARNING disk\nWARNING memory", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "summary\nINFO a\nERROR b\nWARNING c", "expected_output": "Total: 3, Errors: 1, Warnings: 1", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use if/elif to dispatch: if mode == 'count-errors': ...", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Command dispatching pattern", "explanation": "CLI tools dispatch to different logic based on a subcommand. Use if/elif or a dict of functions mapping command → handler.", "code_example": "handlers = {\n    'count-errors': lambda lines: sum(1 for l in lines if l.startswith('ERROR')),\n}\nprint(handlers[mode](log_lines))", "unlocks_after_failures": 3},
        ],
    },
]

LEVEL_8_EXERCISES = LEVEL_8_EXERCISES + make_placeholders("CLI", "CLI Tools", 18, start=3)

# ──────────────────────────────────────────────
# Level 9: Concurrency & Performance
# ──────────────────────────────────────────────

LEVEL_9_EXERCISES = [
    {
        "title": "Benchmark Script Execution Time",
        "problem_statement": "Simulate benchmarking: compute the sum of squares of numbers 1 to N.\nRecord start time (use time.perf_counter()), compute, record end time.\nPrint: 'Result: X\\nTime: Y ms' (Y rounded to 2 decimal places).\nRead N from stdin.",
        "scenario": "Profiling script execution time is the first step in performance optimization.",
        "input_description": "An integer N.",
        "expected_output_description": "Result: X\nTime: Y ms",
        "starter_code": "import time\nn = int(input())\n# Benchmark sum of squares computation\n",
        "tags": ["performance", "timing", "benchmarking"],
        "difficulty": "medium", "xp_reward": 20, "allowed_imports": ["time"], "timeout_secs": 10,
        "test_cases": [
            {"input_data": "1000", "expected_output": "Result: 333833500\nTime: {approx} ms", "is_hidden": False, "comparison_mode": "contains_result"},
        ],
        "hints": [
            {"order_num": 1, "content": "start = time.perf_counter()\n# compute\nend = time.perf_counter()\nelapsed_ms = (end - start) * 1000", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "time.perf_counter() for benchmarking", "explanation": "`time.perf_counter()` provides high-resolution timer. Subtract start from end, multiply by 1000 for milliseconds.", "code_example": "import time\nstart = time.perf_counter()\nresult = sum(i**2 for i in range(1, n+1))\nelapsed = (time.perf_counter() - start) * 1000\nprint(f'Time: {elapsed:.2f} ms')", "unlocks_after_failures": 3},
        ],
    },
]

LEVEL_9_EXERCISES = LEVEL_9_EXERCISES + make_placeholders("Concurrency", "Concurrency", 14, start=2, difficulty="hard", xp=25)

# ──────────────────────────────────────────────
# Level 10: Capstone Projects
# ──────────────────────────────────────────────

LEVEL_10_EXERCISES = [
    {
        "title": "CAPSTONE: Log Monitoring Engine",
        "problem_statement": """Build a log monitoring engine that:\n1. Reads log lines from stdin (format: TIMESTAMP LEVEL SERVICE MESSAGE)\n2. Counts errors per service\n3. Finds the service with most errors\n4. Prints a summary report:\n=== Log Monitoring Report ===\nTotal lines: N\nServices monitored: S\nError summary (sorted by error count desc):\n  service1: N errors\n  service2: N errors\nHighest error rate: service_name\n5. Prints ALERT if any service has > 5 errors""",
        "scenario": "Production log monitoring engines aggregates, classify, and alert on log data from multiple services.",
        "input_description": "Log lines: TIMESTAMP LEVEL SERVICE MESSAGE (one per line)",
        "expected_output_description": "Full monitoring report with alerts.",
        "starter_code": "import sys\nlines = sys.stdin.read().splitlines()\n# Build your log monitoring engine\n",
        "tags": ["capstone", "logs", "dicts", "analysis", "reporting"],
        "difficulty": "hard", "xp_reward": 100, "allowed_imports": ["sys"], "timeout_secs": 10,
        "test_cases": [
            {"input_data": "2024-01-15 ERROR api Connection timeout\n2024-01-15 ERROR api DB failure\n2024-01-15 INFO auth Login ok\n2024-01-15 ERROR worker Job failed\n2024-01-15 ERROR api Rate limit\n2024-01-15 ERROR auth Token expired\n2024-01-15 ERROR api Crash\n2024-01-15 ERROR api OOM\n2024-01-15 ERROR api Timeout2",
             "expected_output": "=== Log Monitoring Report ===\nTotal lines: 9\nServices monitored: 3\nError summary (sorted by error count desc):\n  api: 6 errors\n  auth: 1 errors\n  worker: 1 errors\nHighest error rate: api\nALERT: api has 6 errors",
             "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Parse each line: split into 4 parts. Track error_counts dict by service.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Sort error_counts by value descending. Find max with max(dict, key=dict.get).", "unlock_after_attempts": 2},
            {"order_num": 3, "content": "Set of unique services: track all services seen regardless of level.", "unlock_after_attempts": 3},
        ],
        "concepts": [
            {"title": "Log aggregation engine design", "explanation": "Real log engines collect events, group by dimension (service, level), aggregate (count), then alert on thresholds. This is exactly how Prometheus/Loki work.", "code_example": "error_counts = {}\nservices = set()\nfor line in lines:\n    ts, level, svc, *msg = line.split()\n    services.add(svc)\n    if level == 'ERROR':\n        error_counts[svc] = error_counts.get(svc, 0) + 1", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "CAPSTONE: Config Drift Detector",
        "problem_statement": """Compare two config files (JSON format) provided consecutively on stdin separated by '---'.\nDetect and report:\n1. Keys added (in new, not in old)\n2. Keys removed (in old, not in new)\n3. Keys changed (value different)\nOutput:\n=== Config Drift Report ===\nAdded: key1, key2 (or 'None')\nRemoved: key3 (or 'None')\nChanged:\n  key: old_val → new_val\nDrift detected: YES/NO""",
        "scenario": "Config drift detection finds unauthorized or unintended changes between deployed config versions.",
        "input_description": "Two JSON objects separated by a line containing '---'.",
        "expected_output_description": "Full drift report.",
        "starter_code": "import sys, json\ncontent = sys.stdin.read()\nold_str, new_str = content.split('---')\nold_config = json.loads(old_str)\nnew_config = json.loads(new_str)\n# Detect and report config drift\n",
        "tags": ["capstone", "json", "comparison", "dicts", "devops"],
        "difficulty": "hard", "xp_reward": 100, "allowed_imports": ["sys", "json"], "timeout_secs": 10,
        "test_cases": [
            {"input_data": '{"host": "localhost", "port": 5432, "debug": true, "old_key": "rm"}\n---\n{"host": "prod.db.internal", "port": 5432, "debug": false, "new_key": "added"}',
             "expected_output": "=== Config Drift Report ===\nAdded: new_key\nRemoved: old_key\nChanged:\n  debug: True → False\n  host: localhost → prod.db.internal\nDrift detected: YES",
             "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "added = set(new) - set(old)\nremoved = set(old) - set(new)\nchanged = {k: (old[k], new[k]) for k in old if k in new and old[k] != new[k]}", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Dict diffing pattern", "explanation": "Set operations on dict keys find added/removed. Check matching keys for value differences. This is how Terraform plan and Ansible check mode work.", "code_example": "added = sorted(set(new_config) - set(old_config))\nremoved = sorted(set(old_config) - set(new_config))", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "CAPSTONE: Pod Health Checker",
        "problem_statement": "Read a JSON array of pod status objects (from stdin). Each pod has: name, status (Running/Pending/Failed/CrashLoopBackOff), restarts, cpu_percent, memory_percent.\nGenerate a report:\n=== Kubernetes Pod Health Report ===\nTotal pods: N\nHealthy: N (Running, restarts < 5)\nUnhealthy: N\nCritical pods (Failed or CrashLoopBackOff):\n  - pod_name: status\nHigh restart pods (>= 5):\n  - pod_name: N restarts\nResource alerts (cpu > 80% or memory > 85%):\n  - pod_name: cpu X% memory Y%\nOverall health: HEALTHY/DEGRADED/CRITICAL",
        "scenario": "Kubernetes operators need automated health summaries across hundreds of pods.",
        "input_description": "JSON array of pod objects.",
        "expected_output_description": "Full pod health report.",
        "starter_code": "import sys, json\npods = json.loads(sys.stdin.read())\n# Generate pod health report\n",
        "tags": ["capstone", "kubernetes", "json", "analysis"],
        "difficulty": "hard", "xp_reward": 100, "allowed_imports": ["sys", "json"], "timeout_secs": 10,
        "test_cases": [
            {"input_data": '[{"name":"web-1","status":"Running","restarts":0,"cpu_percent":45,"memory_percent":60},{"name":"db-1","status":"CrashLoopBackOff","restarts":8,"cpu_percent":90,"memory_percent":95},{"name":"cache-1","status":"Running","restarts":2,"cpu_percent":30,"memory_percent":40}]',
             "expected_output": "=== Kubernetes Pod Health Report ===\nTotal pods: 3\nHealthy: 2\nUnhealthy: 1\nCritical pods (Failed or CrashLoopBackOff):\n  - db-1: CrashLoopBackOff\nHigh restart pods (>= 5):\n  - db-1: 8 restarts\nResource alerts (cpu > 80% or memory > 85%):\n  - db-1: cpu 90% memory 95%\nOverall health: CRITICAL",
             "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Separate pods into lists: critical, high_restart, resource_alert. Loop once over all pods filling each list.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Healthy = Running AND restarts < 5. Overall CRITICAL if any critical pod, DEGRADED if warnings only.", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "Multi-dimension health classification", "explanation": "Real health checkers evaluate multiple dimensions: status, restarts, resources. Classify each pod into multiple buckets simultaneously in one pass.", "code_example": "critical, high_restart, resource_alert = [], [], []\nfor pod in pods:\n    if pod['status'] in ('Failed', 'CrashLoopBackOff'):\n        critical.append(pod)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "CAPSTONE: CLI Deployment Automation",
        "problem_statement": "Build a deployment automation script. Read commands from stdin (one per line):\n- deploy <service> <env>: print 'Deploying service to env...\\nDeploy complete: service v1.0 → env'\n- rollback <service>: print 'Rolling back service...\\nRollback complete'\n- status <service>: print 'service: RUNNING (last deploy: 2024-01-15)'\n- help: print list of commands\n- unknown: print 'Unknown command: cmd\\nRun help for usage'\nProcess all commands.",
        "scenario": "A CLI deployment tool automates the most common deployment operations in a single script.",
        "input_description": "Command lines as stdin.",
        "expected_output_description": "Output for each command.",
        "starter_code": "import sys\nlines = sys.stdin.read().splitlines()\n# Process deployment commands\n",
        "tags": ["capstone", "cli", "dispatching", "devops"],
        "difficulty": "hard", "xp_reward": 100, "allowed_imports": ["sys"], "timeout_secs": 10,
        "test_cases": [
            {"input_data": "deploy api prod\nstatus api\nrollback api",
             "expected_output": "Deploying api to prod...\nDeploy complete: api v1.0 → prod\napi: RUNNING (last deploy: 2024-01-15)\nRolling back api...\nRollback complete",
             "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Parse each line with split(). First token is the command. Use if/elif dispatch.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "CLI dispatch table pattern", "explanation": "Map command names to handler functions in a dict. This scales better than if/elif for many commands: `handlers = {'deploy': handle_deploy, ...}`.", "code_example": "for line in lines:\n    parts = line.split()\n    cmd = parts[0]\n    if cmd == 'deploy':\n        svc, env = parts[1], parts[2]\n        print(f'Deploying {svc} to {env}...')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "CAPSTONE: CI/CD Pipeline Simulator",
        "problem_statement": "Simulate a CI/CD pipeline. Read pipeline stages from stdin (one per line: 'stage_name duration_secs result').\nresult is 'pass' or 'fail'.\nProcess each stage:\n- Print '▶ Running: stage_name'\n- If pass: print '✓ stage_name passed (Xs)'\n- If fail: print '✗ stage_name FAILED (Xs)' then print 'Pipeline ABORTED at stage_name' and stop\nAt end (if all pass): print '=== Pipeline SUCCESS ===' and 'Total time: Xs'",
        "scenario": "A CI pipeline executor that runs stages sequentially, stops on failure, and reports timing.",
        "input_description": "Lines: stage_name duration result",
        "expected_output_description": "Stage output lines then success/abort message.",
        "starter_code": "import sys\nlines = sys.stdin.read().splitlines()\n# Simulate CI/CD pipeline execution\n",
        "tags": ["capstone", "cli", "cicd", "loops"],
        "difficulty": "hard", "xp_reward": 100, "allowed_imports": ["sys"], "timeout_secs": 10,
        "test_cases": [
            {"input_data": "build 45 pass\ntest 120 pass\nlint 30 fail\ndeploy 60 pass",
             "expected_output": "▶ Running: build\n✓ build passed (45s)\n▶ Running: test\n✓ test passed (120s)\n▶ Running: lint\n✗ lint FAILED (30s)\nPipeline ABORTED at lint",
             "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "build 45 pass\ntest 60 pass",
             "expected_output": "▶ Running: build\n✓ build passed (45s)\n▶ Running: test\n✓ test passed (60s)\n=== Pipeline SUCCESS ===\nTotal time: 105s",
             "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Track total_time accumulator. Use break on failure. Print success summary only if no break.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Pipeline execution with early exit", "explanation": "Real CI systems stop on first failure (fail-fast). Use `break` to exit the loop when a stage fails. `for/else` pattern handles the success case.", "code_example": "total = 0\nfor line in lines:\n    name, dur, result = line.split()\n    print(f'▶ Running: {name}')\n    if result == 'fail':\n        print(f'✗ {name} FAILED ({dur}s)')\n        print(f'Pipeline ABORTED at {name}')\n        break\n    total += int(dur)\nelse:\n    print('=== Pipeline SUCCESS ===')\n    print(f'Total time: {total}s')", "unlocks_after_failures": 3},
        ],
    },
]
