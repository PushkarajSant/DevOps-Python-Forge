"""
Level 0: Python Execution Basics — 10 exercises
Goal: Understand how Python runs and interacts with environment.
"""

LEVEL_0_EXERCISES = [
    {
        "title": "Hello, DevOps World",
        "problem_statement": "Print the exact text: Hello, DevOps World!",
        "scenario": "Every automation script starts somewhere. Your first task is to confirm Python is running correctly by printing a message to stdout — just like a health check!",
        "input_description": "No input required.",
        "expected_output_description": 'Output must be exactly: Hello, DevOps World!',
        "starter_code": "# Print your message below\n",
        "tags": ["print", "basics"],
        "difficulty": "easy",
        "xp_reward": 5,
        "allowed_imports": [],
        "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "Hello, DevOps World!", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use the `print()` function.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "String literals go inside quotes: `print('Hello, DevOps World!')`", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "print() function", "explanation": "In Python, `print()` sends text to standard output (stdout). This is how scripts communicate results to the terminal and to other programs that consume their output.", "code_example": "print('Hello')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Print System Information",
        "problem_statement": "Print the following two lines exactly:\nOS: Linux\nPython: 3",
        "scenario": "Ops scripts often begin by logging system information. Print a simulated system info header.",
        "input_description": "No input.",
        "expected_output_description": "OS: Linux\nPython: 3",
        "starter_code": "# Print OS and Python version info\n",
        "tags": ["print", "multiline"],
        "difficulty": "easy",
        "xp_reward": 5,
        "allowed_imports": [],
        "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "OS: Linux\nPython: 3", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Call `print()` twice, once for each line.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Multiple print statements", "explanation": "Each `print()` call outputs one line. Calling it multiple times produces multiple lines of output — essential for log-style scripts.", "code_example": "print('Line 1')\nprint('Line 2')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Read and Echo Input",
        "problem_statement": "Read a single line of input from the user and print it back prefixed with 'Input received: '.\nExample: if input is 'deploy', output is 'Input received: deploy'",
        "scenario": "Many DevOps scripts take user input (hostname, environment name, etc.). Practice reading from stdin.",
        "input_description": "A single string on stdin.",
        "expected_output_description": "Input received: <the input string>",
        "starter_code": "# Read input and echo it\n",
        "tags": ["input", "print"],
        "difficulty": "easy",
        "xp_reward": 5,
        "allowed_imports": [],
        "timeout_secs": 3,
        "test_cases": [
            {"input_data": "deploy", "expected_output": "Input received: deploy", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "production", "expected_output": "Input received: production", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "k8s-cluster-1", "expected_output": "Input received: k8s-cluster-1", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `input()` to read from stdin.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Combine the prefix with the input: `print('Input received: ' + value)`", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "input() function", "explanation": "`input()` reads a line from stdin and returns it as a string. In scripts, stdin is often piped from other commands or entered by the operator.", "code_example": "name = input()\nprint('Hello, ' + name)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Basic Arithmetic — CPU Cores",
        "problem_statement": "You have 4 servers, each with 8 CPU cores. Print the total number of CPU cores.",
        "scenario": "Capacity planning requires quick calculations. Calculate total CPU capacity for your cluster.",
        "input_description": "No input.",
        "expected_output_description": "32",
        "starter_code": "servers = 4\ncores_per_server = 8\n# Calculate and print total cores\n",
        "tags": ["arithmetic", "variables"],
        "difficulty": "easy",
        "xp_reward": 5,
        "allowed_imports": [],
        "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "32", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Multiply `servers` by `cores_per_server`.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Use `print(servers * cores_per_server)`", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "Arithmetic operators", "explanation": "Python supports `+`, `-`, `*`, `/`, `//` (floor div), `%` (modulo), `**` (power). For integer results, use `*` for multiplication.", "code_example": "total = 4 * 8\nprint(total)  # 32", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Format Log Message",
        "problem_statement": "Given a server name and status, print a formatted log line.\nPrint: [INFO] server-01 status: online",
        "scenario": "Structured log messages are a core part of any monitoring script.",
        "input_description": "No input — use hardcoded values: server='server-01', status='online'",
        "expected_output_description": "[INFO] server-01 status: online",
        "starter_code": "server = 'server-01'\nstatus = 'online'\n# Print formatted log line\n",
        "tags": ["string-formatting", "print", "logs"],
        "difficulty": "easy",
        "xp_reward": 5,
        "allowed_imports": [],
        "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "[INFO] server-01 status: online", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use an f-string: `f'[INFO] {server} status: {status}'`", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "f-strings (formatted string literals)", "explanation": "f-strings let you embed variables directly inside strings using `{variable}` syntax. They're the modern, readable way to format output in Python.", "code_example": "server = 'web-01'\nstatus = 'online'\nprint(f'[INFO] {server} status: {status}')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Memory Percentage",
        "problem_statement": "Given total_memory=16 and used_memory=12, calculate and print the memory usage percentage.\nPrint as integer: 75",
        "scenario": "Memory monitoring scripts need to calculate usage percentages to trigger alerts.",
        "input_description": "No input — use hardcoded values.",
        "expected_output_description": "75",
        "starter_code": "total_memory = 16\nused_memory = 12\n# Calculate percentage and print as integer\n",
        "tags": ["arithmetic", "variables"],
        "difficulty": "easy",
        "xp_reward": 5,
        "allowed_imports": [],
        "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "75", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Percentage = (used / total) * 100", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Use `int()` to convert to integer before printing.", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "Integer division and conversion", "explanation": "In Python 3, `/` always returns a float. Use `int()` to truncate to integer, or `//` for floor division.", "code_example": "pct = int((12 / 16) * 100)\nprint(pct)  # 75", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Port Number Input",
        "problem_statement": "Read a port number from input, add 1000 to it, and print the result.",
        "scenario": "You need to offset a port number for a staging environment — staging always uses prod port + 1000.",
        "input_description": "A single integer (port number, e.g. 8080).",
        "expected_output_description": "The port number plus 1000.",
        "starter_code": "# Read port, add 1000, print result\n",
        "tags": ["input", "type-casting", "arithmetic"],
        "difficulty": "easy",
        "xp_reward": 5,
        "allowed_imports": [],
        "timeout_secs": 3,
        "test_cases": [
            {"input_data": "8080", "expected_output": "9080", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "443", "expected_output": "1443", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "3000", "expected_output": "4000", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "`input()` returns a string — convert it to int first with `int()`.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "port = int(input())\nprint(port + 1000)", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "Type casting: str to int", "explanation": "`input()` always returns a string. To do arithmetic, you must cast with `int()`. Forgetting this is one of the most common Python bugs in ops scripts.", "code_example": "port = int(input())\nprint(port + 1000)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Uptime Display",
        "problem_statement": "Given uptime_hours=72, print: Server uptime: 72 hours (3 days)",
        "scenario": "Ops dashboards display uptime in a human-readable format.",
        "input_description": "No input.",
        "expected_output_description": "Server uptime: 72 hours (3 days)",
        "starter_code": "uptime_hours = 72\n# Calculate days and print formatted message\n",
        "tags": ["arithmetic", "string-formatting"],
        "difficulty": "easy",
        "xp_reward": 5,
        "allowed_imports": [],
        "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "Server uptime: 72 hours (3 days)", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "days = uptime_hours // 24", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Floor division //", "explanation": "`//` performs floor (integer) division — it divides and rounds down. Useful when converting hours to days, bytes to kilobytes, etc.", "code_example": "hours = 72\ndays = hours // 24  # 3\nprint(f'{hours} hours ({days} days)')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Environment Name Builder",
        "problem_statement": "Read two inputs: project name and environment (e.g. 'myapp' and 'prod').\nPrint: Deploying myapp to prod environment",
        "scenario": "Deployment scripts construct environment-specific target strings from configuration inputs.",
        "input_description": "Two lines of input: project name, then environment name.",
        "expected_output_description": "Deploying <project> to <env> environment",
        "starter_code": "# Read project and environment, print deployment message\n",
        "tags": ["input", "string-formatting"],
        "difficulty": "easy",
        "xp_reward": 5,
        "allowed_imports": [],
        "timeout_secs": 3,
        "test_cases": [
            {"input_data": "myapp\nprod", "expected_output": "Deploying myapp to prod environment", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "api-service\nstaging", "expected_output": "Deploying api-service to staging environment", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Call `input()` twice to read two separate values.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "project = input()\nenv = input()\nprint(f'Deploying {project} to {env} environment')", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "Reading multiple inputs", "explanation": "Call `input()` once per line of stdin. Scripts that accept multiple parameters need multiple `input()` calls (or can split a single line).", "code_example": "project = input()\nenv = input()\nprint(f'Deploying {project} to {env}')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Disk Space Remaining",
        "problem_statement": "Given total_disk=500 and used_disk=320 (in GB), print:\nUsed: 320 GB\nFree: 180 GB\nUsage: 64%",
        "scenario": "Disk monitoring scripts need to report used, free, and percentage at a glance.",
        "input_description": "No input.",
        "expected_output_description": "Used: 320 GB\nFree: 180 GB\nUsage: 64%",
        "starter_code": "total_disk = 500\nused_disk = 320\n# Calculate and print disk stats\n",
        "tags": ["arithmetic", "string-formatting", "print"],
        "difficulty": "easy",
        "xp_reward": 5,
        "allowed_imports": [],
        "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "Used: 320 GB\nFree: 180 GB\nUsage: 64%", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "free = total_disk - used_disk\nUsage% = int((used_disk/total_disk)*100)", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Computing multiple derived values", "explanation": "From two input values you can derive many statistics. Structure your output clearly using multiple `print()` calls with f-strings.", "code_example": "free = 500 - 320\nusage = int((320/500)*100)\nprint(f'Free: {free} GB')\nprint(f'Usage: {usage}%')", "unlocks_after_failures": 3},
        ],
    },
]
