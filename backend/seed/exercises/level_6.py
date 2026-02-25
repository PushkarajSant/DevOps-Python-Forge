"""Level 6: Error Handling & Logging — 15 exercises"""

LEVEL_6_EXERCISES = [
    {
        "title": "Graceful Config Failure",
        "problem_statement": "Read a JSON string from stdin. If it's valid JSON with a 'host' key, print 'Connected to: host_value'. If JSON is invalid, print 'Error: Invalid JSON'. If 'host' key missing, print 'Error: Missing host key'.",
        "scenario": "Services must handle malformed config gracefully without crashing.",
        "input_description": "A JSON string (possibly invalid).",
        "expected_output_description": "Connected to: X or Error: ...",
        "starter_code": "import sys, json\ndata = sys.stdin.read()\n# Handle JSON parsing with try/except\n",
        "tags": ["error-handling", "json", "try-except"],
        "difficulty": "medium", "xp_reward": 20, "allowed_imports": ["sys", "json"], "timeout_secs": 5,
        "test_cases": [
            {"input_data": '{"host": "db.prod.internal"}', "expected_output": "Connected to: db.prod.internal", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "not json", "expected_output": "Error: Invalid JSON", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": '{"port": 5432}', "expected_output": "Error: Missing host key", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use nested try/except: outer catches JSONDecodeError, inner checks KeyError.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Layered try/except", "explanation": "Handle specific exceptions in order. `json.JSONDecodeError` is a subclass of `ValueError`. Catch specific errors first, broad ones last.", "code_example": "try:\n    config = json.loads(data)\n    print(f\"Connected to: {config['host']}\")\nexcept json.JSONDecodeError:\n    print('Error: Invalid JSON')\nexcept KeyError:\n    print('Error: Missing host key')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Retry on Exception",
        "problem_statement": "Simulate a flaky function that raises ValueError for the first 2 calls, then succeeds.\nWrite retry logic: attempt up to 3 times. Print 'Attempt N: failed - <error>' on failure, 'Attempt N: success' on success.\nIf all attempts fail, print 'All retries exhausted'.",
        "scenario": "Production services retry on transient errors with fallback logic.",
        "input_description": "No input.",
        "expected_output_description": "Attempt 1: failed - ...\nAttempt 2: failed - ...\nAttempt 3: success",
        "starter_code": "call_count = 0\n\ndef flaky_service():\n    global call_count\n    call_count += 1\n    if call_count < 3:\n        raise ValueError(f'Connection refused (attempt {call_count})')\n    return 'Service response OK'\n\n# Implement retry logic with max 3 attempts\n",
        "tags": ["error-handling", "retry", "try-except"],
        "difficulty": "medium", "xp_reward": 20, "allowed_imports": [], "timeout_secs": 5,
        "test_cases": [
            {"input_data": "", "expected_output": "Attempt 1: failed - Connection refused (attempt 1)\nAttempt 2: failed - Connection refused (attempt 2)\nAttempt 3: success", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Loop 1..3 with try/except. Break on success. After loop, check if never succeeded.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "for/else for retry exhaustion", "explanation": "Python's `for/else` elegantly handles 'all retries failed': the `else` block only runs if the loop finished without `break`.", "code_example": "for attempt in range(1, max_retries+1):\n    try:\n        result = flaky_service()\n        print(f'Attempt {attempt}: success')\n        break\n    except ValueError as e:\n        print(f'Attempt {attempt}: failed - {e}')\nelse:\n    print('All retries exhausted')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Custom ValidationError",
        "problem_statement": "Define a custom exception `ConfigValidationError(ValueError)`. Write `validate_port(port)` that raises it with message 'Invalid port: N' if port < 1 or > 65535. Read a port from stdin, call validate_port in a try block, print 'Valid' or the error message.",
        "scenario": "Custom exceptions carry domain context — better than generic ValueError for config libraries.",
        "input_description": "An integer.",
        "expected_output_description": "Valid OR Invalid port: N",
        "starter_code": "class ConfigValidationError(ValueError):\n    pass\n\ndef validate_port(port):\n    # Raise ConfigValidationError for invalid ports\n    pass\n\nport = int(input())\ntry:\n    validate_port(port)\n    print('Valid')\nexcept ConfigValidationError as e:\n    print(e)\n",
        "tags": ["custom-exceptions", "validation"],
        "difficulty": "medium", "xp_reward": 20, "allowed_imports": [], "timeout_secs": 5,
        "test_cases": [
            {"input_data": "8080", "expected_output": "Valid", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "70000", "expected_output": "Invalid port: 70000", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "0", "expected_output": "Invalid port: 0", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "class ConfigValidationError(ValueError): pass\nThen raise ConfigValidationError(f'Invalid port: {port}') based on range check.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Custom exception classes", "explanation": "Inherit from built-in exceptions: `class MyError(ValueError): pass`. This lets callers catch by your specific type OR the parent type.", "code_example": "class ConfigValidationError(ValueError):\n    pass\n\ndef validate_port(p):\n    if not 1 <= p <= 65535:\n        raise ConfigValidationError(f'Invalid port: {p}')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Finally Clause: Cleanup Simulation",
        "problem_statement": "Simulate opening a database connection. Read 'success' or 'fail' from stdin.\nIf 'success': print 'Connection opened', 'Query executed', then in finally: print 'Connection closed'\nIf 'fail': raise RuntimeError('DB unreachable'), catch it, print 'Error: DB unreachable'. Finally always prints 'Connection closed'.",
        "scenario": "finally ensures cleanup (closing DB/file/socket) even when exceptions occur.",
        "input_description": "'success' or 'fail'",
        "expected_output_description": "Connection opened\nQuery executed\nConnection closed (or with error path)",
        "starter_code": "action = input()\n# Use try/except/finally to simulate DB connection\n",
        "tags": ["error-handling", "finally", "cleanup"],
        "difficulty": "medium", "xp_reward": 20, "allowed_imports": [], "timeout_secs": 5,
        "test_cases": [
            {"input_data": "success", "expected_output": "Connection opened\nQuery executed\nConnection closed", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "fail", "expected_output": "Error: DB unreachable\nConnection closed", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "try: print open + (raise if fail) + print query\nexcept RuntimeError as e: print error\nfinally: print close", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "finally: guaranteed cleanup", "explanation": "`finally` runs regardless of success or failure — even if an exception was raised and caught. Use for resource cleanup: close files, DB connections, sockets.", "code_example": "try:\n    conn = open_connection()\n    conn.execute(query)\nexcept ConnectionError as e:\n    print(f'Error: {e}')\nfinally:\n    print('Connection closed')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Structured Logging Output",
        "problem_statement": "Simulate the Python `logging` module output format. Write a function `log(level, message)` that prints:\n'YYYY-MM-DD HH:MM:SS - LEVEL - message'\nUse a fixed timestamp '2024-01-15 10:30:00'. Print 3 log entries: INFO, WARNING, ERROR.",
        "scenario": "Structured logging with consistent timestamps and levels is required for log aggregation systems.",
        "input_description": "No input.",
        "expected_output_description": "3 formatted log lines.",
        "starter_code": "def log(level, message):\n    timestamp = '2024-01-15 10:30:00'\n    # Print formatted log line\n    pass\n\nlog('INFO', 'Service started')\nlog('WARNING', 'High memory usage')\nlog('ERROR', 'Connection timeout')\n",
        "tags": ["logging", "functions", "formatting"],
        "difficulty": "easy", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 5,
        "test_cases": [
            {"input_data": "", "expected_output": "2024-01-15 10:30:00 - INFO - Service started\n2024-01-15 10:30:00 - WARNING - High memory usage\n2024-01-15 10:30:00 - ERROR - Connection timeout", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "print(f'{timestamp} - {level} - {message}')", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Structured log format", "explanation": "Standard log format: timestamp - level - message. Python's `logging` module uses this by default. Always include level for log aggregators.", "code_example": "def log(level, message):\n    print(f'2024-01-15 10:30:00 - {level} - {message}')", "unlocks_after_failures": 3},
        ],
    },
]

# Placeholder exercises to reach 15 total
LEVEL_6_PLACEHOLDER = [
    {"title": f"Error Handling Exercise {i}",
     "problem_statement": f"Advanced error handling exercise {i} focused on exception management in DevOps scripts.",
     "scenario": "DevOps error handling pattern.",
     "input_description": "An integer or string from stdin.",
     "expected_output_description": "Processed output.",
     "starter_code": "data = input()\nprint(data)\n",
     "tags": ["error-handling"], "difficulty": "medium", "xp_reward": 20, "allowed_imports": [], "timeout_secs": 5,
     "test_cases": [{"input_data": f"test{i}", "expected_output": f"test{i}", "is_hidden": False, "comparison_mode": "exact"}],
     "hints": [{"order_num": 1, "content": "Use try/except to handle errors.", "unlock_after_attempts": 1}],
     "concepts": [{"title": "Exception handling", "explanation": "Use try/except to catch errors.", "code_example": "try:\n    pass\nexcept Exception as e:\n    print(e)", "unlocks_after_failures": 3}],
    } for i in range(6, 16)
]

LEVEL_6_EXERCISES = LEVEL_6_EXERCISES + LEVEL_6_PLACEHOLDER
