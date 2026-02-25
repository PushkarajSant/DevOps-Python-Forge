"""
Level 4: Functions & Modular Thinking — 20 exercises
Topics: def, parameters, defaults, return values, scope, docstrings
"""

LEVEL_4_EXERCISES = [
    {
        "title": "Reusable Log Formatter",
        "problem_statement": "Write a function `format_log(level, message)` that returns a formatted string:\n'[LEVEL] message'\nCall it with ('INFO', 'Deploy started') and print the result.",
        "scenario": "Centralizing log formatting in a function ensures consistent log structure across scripts.",
        "input_description": "No input.",
        "expected_output_description": "[INFO] Deploy started",
        "starter_code": "def format_log(level, message):\n    # Return formatted log string\n    pass\n\nprint(format_log('INFO', 'Deploy started'))\n",
        "tags": ["functions", "return", "logs"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "requires_function": "format_log",
        "test_cases": [
            {"input_data": "", "expected_output": "[INFO] Deploy started", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `return f'[{level}] {message}'` inside the function.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Functions with return", "explanation": "A function without `return` outputs `None`. Always explicitly `return` the result. The caller then uses the returned value.", "code_example": "def format_log(level, message):\n    return f'[{level}] {message}'\n\nprint(format_log('INFO', 'started'))", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "IP Validator Function",
        "problem_statement": "Write `is_valid_ip(ip)` that returns True if the string is a valid IPv4 address (4 octets, 0-255), False otherwise.\nRead an IP from input, call the function, and print True or False.",
        "scenario": "Reusable validators are essential in any config parsing or networking library.",
        "input_description": "An IP string.",
        "expected_output_description": "True or False",
        "starter_code": "def is_valid_ip(ip):\n    # Return True if valid IPv4, False otherwise\n    pass\n\nip = input()\nprint(is_valid_ip(ip))\n",
        "tags": ["functions", "validation", "networking"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "requires_function": "is_valid_ip",
        "test_cases": [
            {"input_data": "192.168.1.1", "expected_output": "True", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "256.0.0.1", "expected_output": "False", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "10.0.0", "expected_output": "False", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "not-an-ip", "expected_output": "False", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Split on '.', check len==4, then int() each part checking 0-255.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Wrap int() in try/except to handle non-numeric parts.", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "Early return for validation", "explanation": "Validators use early `return False` for each failure condition. The only `return True` is at the end after all checks pass.", "code_example": "def is_valid_ip(ip):\n    parts = ip.split('.')\n    if len(parts) != 4:\n        return False\n    for p in parts:\n        try:\n            if not 0 <= int(p) <= 255:\n                return False\n        except ValueError:\n            return False\n    return True", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Default Parameter: Retry Config",
        "problem_statement": "Write `print_retry_config(service, max_retries=3, delay_secs=5)` that prints:\nService: <service>\nMax retries: <n>\nDelay: <n>s\nCall it twice: once with defaults, once with max_retries=5, delay_secs=10.",
        "scenario": "Default parameters allow scripts to work with sensible defaults but be customizable.",
        "input_description": "No input.",
        "expected_output_description": "Service: api-gateway\nMax retries: 3\nDelay: 5s\nService: db-service\nMax retries: 5\nDelay: 10s",
        "starter_code": "def print_retry_config(service, max_retries=3, delay_secs=5):\n    # Print retry config\n    pass\n\nprint_retry_config('api-gateway')\nprint_retry_config('db-service', max_retries=5, delay_secs=10)\n",
        "tags": ["functions", "default-params"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "requires_function": "print_retry_config",
        "test_cases": [
            {"input_data": "", "expected_output": "Service: api-gateway\nMax retries: 3\nDelay: 5s\nService: db-service\nMax retries: 5\nDelay: 10s", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Default params go in the function signature: `def f(a, b=10):`. Print, don't return.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Default parameter values", "explanation": "Defaults allow callers to omit arguments. Default values must be immutable (int, str, tuple) — never use mutable defaults like `[]` or `{}`.", "code_example": "def connect(host, port=5432, timeout=30):\n    print(f'Connecting to {host}:{port}')\nconnect('localhost')  # uses defaults", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Health Check Function",
        "problem_statement": "Write `check_health(cpu, memory, disk, thresholds={'cpu':85,'memory':80,'disk':90})` that returns a list of metrics exceeding their thresholds.\nRead cpu, memory, disk from input. Print each failing metric on its own line, or 'All healthy' if none.",
        "scenario": "Health checkers compare live metrics against configurable thresholds — a core monitoring pattern.",
        "input_description": "Three integers: cpu, memory, disk (one per line).",
        "expected_output_description": "Failing metric names or 'All healthy'.",
        "starter_code": "def check_health(cpu, memory, disk, thresholds=None):\n    if thresholds is None:\n        thresholds = {'cpu': 85, 'memory': 80, 'disk': 90}\n    # Return list of failing metrics\n    pass\n\ncpu = int(input())\nmemory = int(input())\ndisk = int(input())\nresult = check_health(cpu, memory, disk)\nif result:\n    for m in result:\n        print(m)\nelse:\n    print('All healthy')\n",
        "tags": ["functions", "dicts", "monitoring"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "requires_function": "check_health",
        "test_cases": [
            {"input_data": "90\n70\n88", "expected_output": "cpu", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "50\n60\n70", "expected_output": "All healthy", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "90\n85\n95", "expected_output": "cpu\nmemory\ndisk", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Never use mutable default args! Use `None` and set inside the function.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Build a dict of values: `metrics = {'cpu': cpu, ...}` then compare each with thresholds.", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "Mutable default argument anti-pattern", "explanation": "Never use `def f(x=[])` — the list is shared across calls! Use `None` as default and create inside: `if x is None: x = []`.", "code_example": "def check(*, thresholds=None):\n    if thresholds is None:\n        thresholds = {'cpu': 85}", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Retry Wrapper Function",
        "problem_statement": "Write `simulate_retry(task_name, max_attempts)` that simulates retry logic:\nPrint 'Attempt N: failed' for each attempt except the last.\nPrint 'Attempt N: success' for the last attempt.\nReturn the number of attempts.\nCall with ('deploy', 4) and print 'Completed in N attempts'.",
        "scenario": "Retry wrappers abstract retry logic so individual tasks don't implement it themselves.",
        "input_description": "No input.",
        "expected_output_description": "Attempt 1: failed...Attempt 4: success\nCompleted in 4 attempts",
        "starter_code": "def simulate_retry(task_name, max_attempts):\n    # Simulate retry and return attempt count\n    pass\n\ncount = simulate_retry('deploy', 4)\nprint(f'Completed in {count} attempts')\n",
        "tags": ["functions", "loops", "return", "devops"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "requires_function": "simulate_retry",
        "test_cases": [
            {"input_data": "", "expected_output": "Attempt 1: failed\nAttempt 2: failed\nAttempt 3: failed\nAttempt 4: success\nCompleted in 4 attempts", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Loop from 1 to max_attempts. Print 'failed' if not the last, 'success' if last. Return the count.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Functions with side effects and return", "explanation": "A function can both print output (side effect) AND return a value. These are orthogonal — callers use the return value; output goes to stdout.", "code_example": "def simulate(name, n):\n    for i in range(1, n+1):\n        if i == n:\n            print(f'Attempt {i}: success')\n        else:\n            print(f'Attempt {i}: failed')\n    return n", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Config Key Validator",
        "problem_statement": "Write `validate_config(config, required_keys)` that returns a list of MISSING required keys.\nTest with config={'host':'localhost','port':5432} and required=['host','port','database','user'].\nPrint each missing key or 'Config valid' if none missing.",
        "scenario": "Before connecting to a database, validate that all required config keys are present.",
        "input_description": "No input.",
        "expected_output_description": "database\nuser",
        "starter_code": "def validate_config(config, required_keys):\n    # Return list of missing keys\n    pass\n\nconfig = {'host': 'localhost', 'port': 5432}\nrequired = ['host', 'port', 'database', 'user']\nmissing = validate_config(config, required)\nif missing:\n    for key in missing:\n        print(key)\nelse:\n    print('Config valid')\n",
        "tags": ["functions", "dicts", "validation"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "requires_function": "validate_config",
        "test_cases": [
            {"input_data": "", "expected_output": "database\nuser", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Return `[k for k in required_keys if k not in config]`", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "List comprehension as filter return", "explanation": "Functions can return list comprehensions directly: `return [k for k in required if k not in config]`. Concise and readable.", "code_example": "def validate_config(config, required):\n    return [k for k in required if k not in config]", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Bytes Formatter with Unit Selection",
        "problem_statement": "Write `format_bytes(n, unit='auto')` that formats bytes:\n- unit='KB': divide by 1024\n- unit='MB': divide by 1024^2\n- unit='GB': divide by 1024^3\n- unit='auto': pick best unit\nReturn formatted string like '1.50 MB'. Print result for bytes=1572864.",
        "scenario": "Ops scripts display file sizes in the most appropriate unit without hardcoding the scale.",
        "input_description": "No input.",
        "expected_output_description": "1.50 MB",
        "starter_code": "def format_bytes(n, unit='auto'):\n    # Return formatted bytes string\n    pass\n\nprint(format_bytes(1572864))\n",
        "tags": ["functions", "default-params", "arithmetic"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "requires_function": "format_bytes",
        "test_cases": [
            {"input_data": "", "expected_output": "1.50 MB", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "For 'auto': if n >= 1024^3 use GB, elif >= 1024^2 use MB, elif >= 1024 use KB.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Auto-scaling unit selection", "explanation": "Check thresholds from largest to smallest. Return as soon as the right unit is identified. Format with `:.2f`.", "code_example": "def format_bytes(n, unit='auto'):\n    if unit == 'auto':\n        if n >= 1024**3:\n            return f'{n/1024**3:.2f} GB'\n        elif n >= 1024**2:\n            return f'{n/1024**2:.2f} MB'\n        else:\n            return f'{n/1024:.2f} KB'", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Docstring Convention",
        "problem_statement": "Write `get_server_info(hostname, port, protocol='http')` with a proper docstring.\nReturn a dict: {'url': 'http://hostname:port', 'hostname': hostname, 'port': port, 'protocol': protocol}.\nPrint the url from the returned dict when called with ('api.example.com', 8080).",
        "scenario": "Documented functions are production-grade. Every reusable ops function should have a docstring.",
        "input_description": "No input.",
        "expected_output_description": "http://api.example.com:8080",
        "starter_code": "def get_server_info(hostname, port, protocol='http'):\n    \"\"\"\n    Build server info dict.\n    \n    Args:\n        hostname: Server hostname\n        port: Server port\n        protocol: Protocol (default: http)\n    \n    Returns:\n        dict with url, hostname, port, protocol\n    \"\"\"\n    # Return server info dict\n    pass\n\ninfo = get_server_info('api.example.com', 8080)\nprint(info['url'])\n",
        "tags": ["functions", "docstrings", "return", "dicts"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "requires_function": "get_server_info",
        "test_cases": [
            {"input_data": "", "expected_output": "http://api.example.com:8080", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Return `{'url': f'{protocol}://{hostname}:{port}', ...}`", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Docstrings for production functions", "explanation": "Docstrings (triple-quoted strings after `def`) document what a function does, its parameters, and return value. They're accessible via `help(func)`.", "code_example": "def greet(name):\n    \"\"\"Return a greeting string.\"\"\"\n    return f'Hello, {name}'", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Variable Scope: Local vs Global",
        "problem_statement": "The code below has a bug. Fix it so `update_count()` increments the global `request_count` and `get_count()` returns it.\nAfter calling update_count() 3 times, print get_count(). Expected: 3",
        "scenario": "Global state management is needed in scripts that maintain counters across function calls.",
        "input_description": "No input.",
        "expected_output_description": "3",
        "starter_code": "request_count = 0\n\ndef update_count():\n    # Fix: increment global request_count\n    request_count += 1\n\ndef get_count():\n    return request_count\n\nupdate_count()\nupdate_count()\nupdate_count()\nprint(get_count())\n",
        "tags": ["functions", "scope", "global"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "3", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Add `global request_count` at the start of `update_count()`.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "global keyword for mutation", "explanation": "Inside a function, `x = 1` creates a LOCAL variable. To modify a global variable, declare `global x` first. Otherwise Python assumes local scope.", "code_example": "count = 0\ndef increment():\n    global count\n    count += 1", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Multiple Return Values",
        "problem_statement": "Write `analyze_logs(log_list)` that returns (total, error_count, warning_count) as a tuple.\nLines starting with 'ERROR' count as errors, 'WARN' as warnings.\nPrint: Total: N, Errors: N, Warnings: N",
        "scenario": "Log analysis functions return multiple statistics in one call instead of separate passes.",
        "input_description": "No input — use the hardcoded list below.",
        "expected_output_description": "Total: 5, Errors: 2, Warnings: 1",
        "starter_code": "def analyze_logs(log_list):\n    # Return (total, error_count, warning_count)\n    pass\n\nlogs = [\n    'INFO service started',\n    'ERROR disk full',\n    'WARN memory high',\n    'INFO checkpoint',\n    'ERROR connection timeout'\n]\ntotal, errors, warnings = analyze_logs(logs)\nprint(f'Total: {total}, Errors: {errors}, Warnings: {warnings}')\n",
        "tags": ["functions", "multiple-return", "logs"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "requires_function": "analyze_logs",
        "test_cases": [
            {"input_data": "", "expected_output": "Total: 5, Errors: 2, Warnings: 1", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Return a tuple: `return (total, error_count, warning_count)`. Unpack with `a, b, c = func()`.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Multiple return values via tuples", "explanation": "Python functions can return multiple values as a tuple: `return a, b, c`. The caller unpacks: `x, y, z = func()`. This avoids creating wrapper objects.", "code_example": "def stats(data):\n    return len(data), sum(data), sum(data)/len(data)\n\nn, total, avg = stats([1,2,3])", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Recursive Directory Size",
        "problem_statement": "Write `factorial(n)` recursively. Then use it to compute how many possible orderings (n!) exist for n services in a deployment pipeline.\nRead n from input, print: n! = <result>",
        "scenario": "Recursive thinking: deployment ordering — how many possible sequences for 5 services?",
        "input_description": "An integer N.",
        "expected_output_description": "5! = 120",
        "starter_code": "def factorial(n):\n    # Recursive factorial\n    pass\n\nn = int(input())\nprint(f'{n}! = {factorial(n)}')\n",
        "tags": ["functions", "recursion"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "requires_function": "factorial",
        "test_cases": [
            {"input_data": "5", "expected_output": "5! = 120", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "0", "expected_output": "0! = 1", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "10", "expected_output": "10! = 3628800", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Base case: if n == 0 or n == 1: return 1\nRecursive case: return n * factorial(n-1)", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Recursion: base case + recursive case", "explanation": "Every recursive function needs: (1) a base case that returns without recursing, (2) a recursive call that moves toward the base case.", "code_example": "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Lambda for Sorting",
        "problem_statement": "Given a list of deployment records (dicts with 'service', 'deploy_time', 'status'), sort by deploy_time ascending using a lambda.\nPrint each as: service: Xs (status)",
        "scenario": "Deployment logs sorted by time help trace the deployment order during incident review.",
        "input_description": "No input.",
        "expected_output_description": "auth: 12s (success)\napi: 45s (success)\ndb: 120s (failed)",
        "starter_code": "deployments = [\n    {'service': 'api', 'deploy_time': 45, 'status': 'success'},\n    {'service': 'db', 'deploy_time': 120, 'status': 'failed'},\n    {'service': 'auth', 'deploy_time': 12, 'status': 'success'},\n]\n# Sort by deploy_time with a lambda and print\n",
        "tags": ["functions", "lambda", "sorting"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "auth: 12s (success)\napi: 45s (success)\ndb: 120s (failed)", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "sorted(deployments, key=lambda d: d['deploy_time'])", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Lambda functions for sort keys", "explanation": "Lambda is an anonymous single-expression function. `lambda x: x['field']` is a concise key extractor for sorting.", "code_example": "sorted_list = sorted(items, key=lambda x: x['time'])", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Higher-Order Function: apply_to_servers",
        "problem_statement": "Write `apply_to_servers(servers, operation)` that applies `operation` (a function) to each server name and returns the results as a list.\nUse it with: (1) str.upper to uppercase all (2) a lambda that appends ':8080'\nPrint results of both calls.",
        "scenario": "Higher-order functions let you apply arbitary operations to server lists — foundation of map/filter patterns.",
        "input_description": "No input.",
        "expected_output_description": "WEB-01\nWEB-02\nDB-01\nweb-01:8080\nweb-02:8080\ndb-01:8080",
        "starter_code": "def apply_to_servers(servers, operation):\n    # Apply operation to each server and return list\n    pass\n\nservers = ['web-01', 'web-02', 'db-01']\nupper = apply_to_servers(servers, str.upper)\nfor s in upper:\n    print(s)\nwith_port = apply_to_servers(servers, lambda s: s + ':8080')\nfor s in with_port:\n    print(s)\n",
        "tags": ["functions", "higher-order", "lambda"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "requires_function": "apply_to_servers",
        "test_cases": [
            {"input_data": "", "expected_output": "WEB-01\nWEB-02\nDB-01\nweb-01:8080\nweb-02:8080\ndb-01:8080", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Return `[operation(s) for s in servers]`", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Higher-order functions", "explanation": "A function that takes another function as a parameter is called higher-order. This is the basis of `map()`, `filter()`, and functional programming patterns.", "code_example": "def apply(items, fn):\n    return [fn(x) for x in items]\n\nresult = apply(['a', 'b'], str.upper)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "*args for Multi-Server Ping",
        "problem_statement": "Write `ping_servers(*hosts)` that prints 'Pinging: host' for each host.\nCall it with ('web-01', 'web-02', 'db-01') — must work with any number of args.",
        "scenario": "*args enables functions that accept variable numbers of servers — like a multi-target ping tool.",
        "input_description": "No input.",
        "expected_output_description": "Pinging: web-01\nPinging: web-02\nPinging: db-01",
        "starter_code": "def ping_servers(*hosts):\n    # Print 'Pinging: host' for each host\n    pass\n\nping_servers('web-01', 'web-02', 'db-01')\n",
        "tags": ["functions", "args", "variadic"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "requires_function": "ping_servers",
        "test_cases": [
            {"input_data": "", "expected_output": "Pinging: web-01\nPinging: web-02\nPinging: db-01", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "`*hosts` collects all positional args into a tuple. Loop over it normally.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "*args: variable positional arguments", "explanation": "`*args` in a function signature collects any number of positional arguments into a tuple. Use it when the number of inputs isn't fixed.", "code_example": "def ping(*hosts):\n    for h in hosts:\n        print(f'Pinging: {h}')\n\nping('web-01', 'web-02')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "**kwargs for Config Function",
        "problem_statement": "Write `create_connection(**kwargs)` that prints each configuration key=value in sorted order.\nCall with: host='localhost', port=5432, timeout=30, ssl=True",
        "scenario": "**kwargs allows passing arbitrary config parameters without changing the function signature.",
        "input_description": "No input.",
        "expected_output_description": "host=localhost\nport=5432\nssl=True\ntimeout=30",
        "starter_code": "def create_connection(**kwargs):\n    # Print sorted key=value config\n    pass\n\ncreate_connection(host='localhost', port=5432, timeout=30, ssl=True)\n",
        "tags": ["functions", "kwargs", "config"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "requires_function": "create_connection",
        "test_cases": [
            {"input_data": "", "expected_output": "host=localhost\nport=5432\nssl=True\ntimeout=30", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "`**kwargs` is a dict. Loop with `for k, v in sorted(kwargs.items()):`", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "**kwargs: variable keyword arguments", "explanation": "`**kwargs` collects any number of keyword arguments as a dict. Together with `*args`, it makes fully variadic functions.", "code_example": "def config(**kwargs):\n    for k, v in sorted(kwargs.items()):\n        print(f'{k}={v}')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Pure Function: Deploy Calculator",
        "problem_statement": "Write `calculate_deploy_time(services, avg_secs_per_service, parallel=False, workers=3)` that:\n- If parallel=False: total = services * avg_secs\n- If parallel=True: total = ceil(services / workers) * avg_secs\nReturn total seconds. Print result for (12, 30) and (12, 30, parallel=True).",
        "scenario": "Estimating sequential vs parallel deployment time is essential for release pipeline planning.",
        "input_description": "No input.",
        "expected_output_description": "360\n120",
        "starter_code": "import math\n\ndef calculate_deploy_time(services, avg_secs_per_service, parallel=False, workers=3):\n    # Return total deploy time in seconds\n    pass\n\nprint(calculate_deploy_time(12, 30))\nprint(calculate_deploy_time(12, 30, parallel=True))\n",
        "tags": ["functions", "math", "devops"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": ["math"], "timeout_secs": 3,
        "requires_function": "calculate_deploy_time",
        "test_cases": [
            {"input_data": "", "expected_output": "360\n120", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Sequential: return services * avg_secs\nParallel: return math.ceil(services/workers) * avg_secs", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Pure functions: same input, same output", "explanation": "A pure function produces the same output for the same inputs and has no side effects. They're easy to test and reason about.", "code_example": "def deploy_time(n, t, parallel=False, w=3):\n    if parallel:\n        import math\n        return math.ceil(n/w) * t\n    return n * t", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Function Composition: Log Pipeline",
        "problem_statement": "Write three functions:\n1. `parse_log(line)` → returns dict {level, message} by splitting on first space\n2. `filter_errors(log_dict)` → returns True if level is ERROR\n3. `format_alert(log_dict)` → returns 'ALERT: message'\nCompose them: read N lines, filter errors, format and print each alert.",
        "scenario": "Function composition is the foundation of Unix-pipeline-style log processing.",
        "input_description": "First line: N. Then N log lines.",
        "expected_output_description": "ALERT: message for each ERROR line",
        "starter_code": "def parse_log(line):\n    pass\n\ndef filter_errors(log_dict):\n    pass\n\ndef format_alert(log_dict):\n    pass\n\nimport sys\nlines = sys.stdin.read().splitlines()\nn = int(lines[0])\nfor line in lines[1:n+1]:\n    parsed = parse_log(line)\n    if filter_errors(parsed):\n        print(format_alert(parsed))\n",
        "tags": ["functions", "composition", "logs"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": ["sys"], "timeout_secs": 3,
        "requires_function": "parse_log",
        "test_cases": [
            {"input_data": "3\nINFO service started\nERROR disk full\nWARN high memory", "expected_output": "ALERT: disk full", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "2\nERROR db crash\nERROR network timeout", "expected_output": "ALERT: db crash\nALERT: network timeout", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "parse_log: split on space with maxsplit=1 → {level, message}\nfilter_errors: return log_dict['level'] == 'ERROR'", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Function composition pattern", "explanation": "Chain functions: output of one becomes input of next. This is how Unix pipes work conceptually: `parse → filter → format`. Each function does ONE thing.", "code_example": "def parse_log(line):\n    level, msg = line.split(' ', 1)\n    return {'level': level, 'message': msg}", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Memoization for Repeated Queries",
        "problem_statement": "Write `cached_lookup(host, cache={})` that simulates a slow DNS lookup:\n- If host is in cache, print 'Cache hit: host → ip' and return cached ip\n- Otherwise, compute ip as '10.0.0.' + str(len(cache)+1), print 'Cache miss: host → ip', store in cache, return ip\nLook up: web-01, db-01, web-01, cache-01, db-01",
        "scenario": "Caching DNS lookups prevents repeated expensive queries in automation scripts.",
        "input_description": "No input.",
        "expected_output_description": "Cache miss: web-01 → 10.0.0.1\nCache miss: db-01 → 10.0.0.2\nCache hit: web-01 → 10.0.0.1\nCache miss: cache-01 → 10.0.0.3\nCache hit: db-01 → 10.0.0.2",
        "starter_code": "def cached_lookup(host, cache={}):\n    # Simulate cached DNS lookup\n    pass\n\nfor host in ['web-01', 'db-01', 'web-01', 'cache-01', 'db-01']:\n    cached_lookup(host)\n",
        "tags": ["functions", "memoization", "caching"],
        "difficulty": "hard", "xp_reward": 20, "allowed_imports": [], "timeout_secs": 3,
        "requires_function": "cached_lookup",
        "test_cases": [
            {"input_data": "", "expected_output": "Cache miss: web-01 → 10.0.0.1\nCache miss: db-01 → 10.0.0.2\nCache hit: web-01 → 10.0.0.1\nCache miss: cache-01 → 10.0.0.3\nCache hit: db-01 → 10.0.0.2", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "The mutable dict default `cache={}` persists between calls (unusual but intentional here for caching).", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Function-level cache with mutable default", "explanation": "While mutable defaults are usually a bug, they can intentionally cache data across calls. In production, use `functools.lru_cache` or an explicit cache dict.", "code_example": "def cached_lookup(host, cache={}):\n    if host in cache:\n        print(f'Cache hit: {host} → {cache[host]}')\n    else:\n        ip = f'10.0.0.{len(cache)+1}'\n        cache[host] = ip\n        print(f'Cache miss: {host} → {ip}')\n    return cache[host]", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Generator for Log Streaming",
        "problem_statement": "Write a generator function `log_stream(n)` that yields log lines:\n'[00:00:0N] INFO Processing item N' for N from 1 to n.\nRead N from input, iterate the generator and print each line.",
        "scenario": "Generators stream large log datasets without loading everything into memory — critical for production log processing.",
        "input_description": "An integer N.",
        "expected_output_description": "[00:00:01] INFO Processing item 1\n[00:00:02] INFO Processing item 2\n...",
        "starter_code": "def log_stream(n):\n    # Yield log lines one at a time\n    pass\n\nn = int(input())\nfor line in log_stream(n):\n    print(line)\n",
        "tags": ["functions", "generators", "yield"],
        "difficulty": "hard", "xp_reward": 20, "allowed_imports": [], "timeout_secs": 3,
        "requires_function": "log_stream",
        "test_cases": [
            {"input_data": "3", "expected_output": "[00:00:01] INFO Processing item 1\n[00:00:02] INFO Processing item 2\n[00:00:03] INFO Processing item 3", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `yield` instead of `return`. The function becomes a generator that can be iterated.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Generator functions with yield", "explanation": "A function with `yield` becomes a generator. It produces values lazily, one at a time, without storing all in memory. Ideal for streaming data.", "code_example": "def log_stream(n):\n    for i in range(1, n+1):\n        yield f'[00:00:{i:02d}] INFO Processing item {i}'\n\nfor log in log_stream(5):\n    print(log)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Error-Safe Config Loader",
        "problem_statement": "Write `safe_get(config, key, default=None)` that returns config[key] if it exists, default otherwise. Never raise KeyError.\nAlso write `require_key(config, key)` that raises ValueError('Missing required key: key') if key not in config.\nTest both: use config={'host':'localhost'}, get 'port' (default=5432), require 'host' (should work), require 'database' (should catch and print the error).",
        "scenario": "Safe config access prevents crashes when optional keys are missing while ensuring required keys exist.",
        "input_description": "No input.",
        "expected_output_description": "5432\nlocalhost\nMissing required key: database",
        "starter_code": "def safe_get(config, key, default=None):\n    # Return config[key] or default\n    pass\n\ndef require_key(config, key):\n    # Raise ValueError if key missing\n    pass\n\nconfig = {'host': 'localhost'}\nprint(safe_get(config, 'port', 5432))\nprint(require_key(config, 'host'))\ntry:\n    require_key(config, 'database')\nexcept ValueError as e:\n    print(e)\n",
        "tags": ["functions", "error-handling", "config"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "requires_function": "safe_get",
        "test_cases": [
            {"input_data": "", "expected_output": "5432\nlocalhost\nMissing required key: database", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "safe_get: return config.get(key, default)\nrequire_key: if key not in config: raise ValueError(f'Missing required key: {key}')\nreturn config[key]", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Raising ValueError in validation functions", "explanation": "Use `raise ValueError('message')` to signal missing required inputs. Callers use `try/except ValueError` to handle it gracefully.", "code_example": "def require(config, key):\n    if key not in config:\n        raise ValueError(f'Missing required key: {key}')\n    return config[key]", "unlocks_after_failures": 3},
        ],
    },
]
