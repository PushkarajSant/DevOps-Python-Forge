"""
Level 1: Core Fundamentals — 20 exercises
Topics: Variables, Data Types, Type Casting, Operators, String Formatting
"""

LEVEL_1_EXERCISES = [
    {
        "title": "Variable Types Detective",
        "problem_statement": "Given the following values, print the type of each on a separate line:\n- 42\n- 3.14\n- 'nginx'\n- True\n\nExpected output:\n<class 'int'>\n<class 'float'>\n<class 'str'>\n<class 'bool'>",
        "scenario": "When debugging ops scripts, identifying variable types quickly prevents type-mismatch bugs.",
        "input_description": "No input.",
        "expected_output_description": "<class 'int'>\n<class 'float'>\n<class 'str'>\n<class 'bool'>",
        "starter_code": "# Print the type of each value\n",
        "tags": ["data-types", "type"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "<class 'int'>\n<class 'float'>\n<class 'str'>\n<class 'bool'>", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `type()` on each value and print the result.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Python data types", "explanation": "Python has 4 primitive types: int, float, str, bool. `type(value)` returns the type object. Knowing your types prevents the most common scripting bugs.", "code_example": "print(type(42))    # <class 'int'>\nprint(type(3.14))  # <class 'float'>", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "MB to GB Converter",
        "problem_statement": "Read memory size in MB from input, convert to GB (divide by 1024), and print with 2 decimal places.\nExample: input=2048 → output=2.00 GB",
        "scenario": "Ops scripts regularly convert between memory units for human-readable reports.",
        "input_description": "An integer representing MB.",
        "expected_output_description": "<value> GB (2 decimal places)",
        "starter_code": "# Read MB, convert to GB, print with 2 decimal places\n",
        "tags": ["type-casting", "arithmetic", "string-formatting"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "2048", "expected_output": "2.00 GB", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "512", "expected_output": "0.50 GB", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "1536", "expected_output": "1.50 GB", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "gb = int(input()) / 1024", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Use f-string with format spec: `f'{gb:.2f} GB'`", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "Float formatting with f-strings", "explanation": "Use `:.2f` inside an f-string to format a float to 2 decimal places: `f'{value:.2f}'`", "code_example": "gb = 2048 / 1024\nprint(f'{gb:.2f} GB')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Server Status Report",
        "problem_statement": "Read server name and response time (ms) from two input lines.\nPrint: [STATUS] <server> responded in <ms>ms\nIf ms > 500: also print: WARNING: High latency detected!",
        "scenario": "Latency monitoring: build a script that flags slow servers.",
        "input_description": "Line 1: server name. Line 2: response time in ms (integer).",
        "expected_output_description": "[STATUS] web-01 responded in 300ms (no warning if <=500)",
        "starter_code": "# Read server name and response time, print status\n",
        "tags": ["input", "conditionals", "string-formatting"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "web-01\n300", "expected_output": "[STATUS] web-01 responded in 300ms", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "db-server\n750", "expected_output": "[STATUS] db-server responded in 750ms\nWARNING: High latency detected!", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Read two inputs. Convert ms to int for comparison.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Use `if ms > 500:` to add the warning.", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "Combining input, types, and conditionals", "explanation": "Real ops scripts read config, check thresholds, and emit warnings. This pattern is the foundation of any monitoring script.", "code_example": "ms = int(input())\nif ms > 500:\n    print('WARNING')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "String Operations on Hostnames",
        "problem_statement": "Read a hostname. Print:\n1. It uppercased\n2. Its length\n3. Whether it starts with 'web' (True/False)",
        "scenario": "Parsing and validating hostname strings is common in inventory management scripts.",
        "input_description": "A single hostname string.",
        "expected_output_description": "WEB-SERVER-01\n13\nTrue",
        "starter_code": "# Read hostname, print uppercase, length, and starts-with check\n",
        "tags": ["strings", "methods"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "web-server-01", "expected_output": "WEB-SERVER-01\n13\nTrue", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "db-primary", "expected_output": "DB-PRIMARY\n10\nFalse", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `.upper()`, `len()`, and `.startswith()`", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "String methods", "explanation": "Python strings have built-in methods: `.upper()`, `.lower()`, `.strip()`, `.startswith()`, `.endswith()`, `.split()`, `.replace()`. These are essential for log parsing.", "code_example": "h = 'web-01'\nprint(h.upper())\nprint(len(h))\nprint(h.startswith('web'))", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Bytes to Human Readable",
        "problem_statement": "Read bytes as integer input. Convert and print:\nKB: <value>\nMB: <value>\nGB: <value>\nAll values rounded to 2 decimal places.",
        "scenario": "Ops dashboards display file sizes and network transfer in human-readable format.",
        "input_description": "An integer (bytes).",
        "expected_output_description": "KB: 1024.00\nMB: 1.00\nGB: 0.00",
        "starter_code": "# Read bytes, print KB/MB/GB\n",
        "tags": ["arithmetic", "string-formatting"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "1048576", "expected_output": "KB: 1024.00\nMB: 1.00\nGB: 0.00", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "1073741824", "expected_output": "KB: 1048576.00\nMB: 1024.00\nGB: 1.00", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "KB = bytes/1024, MB = bytes/1024^2, GB = bytes/1024^3", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Unit conversion chains", "explanation": "Divide bytes by 1024 repeatedly to get KB, MB, GB. Use `:.2f` for clean decimal display.", "code_example": "b = 1048576\nprint(f'KB: {b/1024:.2f}')\nprint(f'MB: {b/1024**2:.2f}')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "IP Address Extractor",
        "problem_statement": "Read an IP:port string (e.g. '192.168.1.10:8080').\nPrint:\nIP: 192.168.1.10\nPort: 8080",
        "scenario": "Parsing service endpoints from config files is essential in service mesh scripts.",
        "input_description": "A string in format IP:port",
        "expected_output_description": "IP: <ip>\nPort: <port>",
        "starter_code": "# Parse IP and port from input string\n",
        "tags": ["strings", "split", "parsing"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "192.168.1.10:8080", "expected_output": "IP: 192.168.1.10\nPort: 8080", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "10.0.0.1:443", "expected_output": "IP: 10.0.0.1\nPort: 443", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `.split(':')` to separate IP and port.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "parts = input().split(':')\nip = parts[0]\nport = parts[1]", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "String splitting for parsing", "explanation": "`.split(delimiter)` splits a string into a list at each occurrence of the delimiter. It's the go-to method for parsing structured text like 'host:port'.", "code_example": "endpoint = '10.0.0.1:8080'\nip, port = endpoint.split(':')\nprint('IP:', ip)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Log Level Formatter",
        "problem_statement": "Read level (INFO/WARN/ERROR) and message. Print:\n[INFO]  message\n[WARN]  message\n[ERROR] message\n(Note the alignment — pad to 7 chars including brackets)",
        "scenario": "Consistent log formatting makes logs parseable by tools like ELK stack.",
        "input_description": "Line 1: level. Line 2: message.",
        "expected_output_description": "[INFO]  Deployment started",
        "starter_code": "# Read level and message, print aligned log line\n",
        "tags": ["string-formatting", "alignment", "logs"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "INFO\nDeployment started", "expected_output": "[INFO]  Deployment started", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "ERROR\nService crashed", "expected_output": "[ERROR] Service crashed", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "WARN\nHigh memory", "expected_output": "[WARN]  High memory", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Format the level with brackets first: `f'[{level}]'`, then pad to 7 chars.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Use f-string pad: `f'[{level}]'.ljust(7)`", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "String alignment and padding", "explanation": "`.ljust(n)` left-justifies a string to width n. `.rjust(n)` right-justifies. Essential for creating aligned log output.", "code_example": "tag = f'[INFO]'\nprint(f'{tag.ljust(7)} message')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Boolean Status Check",
        "problem_statement": "Read a number (0 or 1). Print 'Service is running' if 1, 'Service is stopped' if 0.",
        "scenario": "Health check scripts return 0/1 exit codes. Parse and interpret them.",
        "input_description": "A single integer: 0 or 1.",
        "expected_output_description": "Service is running OR Service is stopped",
        "starter_code": "# Read 0 or 1 and print service status\n",
        "tags": ["boolean", "conditionals"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "1", "expected_output": "Service is running", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "0", "expected_output": "Service is stopped", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Convert input to int with `int()`, then use `if`.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Integer as boolean", "explanation": "In Python, `0` is falsy and any non-zero is truthy. You can use `if int(val):` to check.", "code_example": "status = int(input())\nif status:\n    print('running')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Multiple Assignments",
        "problem_statement": "Assign these three variables and print them on one line separated by ' | ':\nhost='api.example.com', port=443, protocol='https'\nOutput: api.example.com | 443 | https",
        "scenario": "Service configuration often bundles host, port, and protocol together.",
        "input_description": "No input.",
        "expected_output_description": "api.example.com | 443 | https",
        "starter_code": "host = 'api.example.com'\nport = 443\nprotocol = 'https'\n# Print all three separated by ' | '\n",
        "tags": ["variables", "string-formatting"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "api.example.com | 443 | https", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use f-string: `f'{host} | {port} | {protocol}'`", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Multi-value f-strings", "explanation": "f-strings can embed multiple variables: `f'{a} | {b} | {c}'`. Mixed types (str and int) work seamlessly.", "code_example": "print(f'{host} | {port} | {protocol}')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Swap Without Temp",
        "problem_statement": "Read two server names. Swap them and print:\nServer A: <original B>\nServer B: <original A>",
        "scenario": "Blue-green deployments require swapping active and idle server roles.",
        "input_description": "Line 1: server A. Line 2: server B.",
        "expected_output_description": "Server A: blue\nServer B: green (when input is green then blue)",
        "starter_code": "# Read two servers, swap them, print result\n",
        "tags": ["variables", "swap"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "green\nblue", "expected_output": "Server A: blue\nServer B: green", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "primary\nstandby", "expected_output": "Server A: standby\nServer B: primary", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Python supports tuple unpacking swap: `a, b = b, a`", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Tuple unpacking swap", "explanation": "Python lets you swap two variables in one line: `a, b = b, a`. No temp variable needed. This is a Pythonic pattern.", "code_example": "a = 'green'\nb = 'blue'\na, b = b, a\nprint(a)  # blue", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Operator Precedence",
        "problem_statement": "Compute: result = 2 + 3 * 4 - 1\nPrint the result.",
        "scenario": "Getting arithmetic right in monitoring threshold calculations requires understanding operator precedence.",
        "input_description": "No input.",
        "expected_output_description": "13",
        "starter_code": "# Compute 2 + 3 * 4 - 1 and print\n",
        "tags": ["operators", "precedence"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "13", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Multiplication happens before addition/subtraction.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Operator precedence (PEMDAS)", "explanation": "Python follows standard math precedence: parentheses first, then exponents, multiply/divide, then add/subtract. `2 + 3*4 - 1 = 2 + 12 - 1 = 13`", "code_example": "result = 2 + 3 * 4 - 1  # 13\nprint(result)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Modulo for Even/Odd Detection",
        "problem_statement": "Read a port number. Print 'Even port' or 'Odd port'.",
        "scenario": "Port assignment scripts sometimes allocate even ports for primaries and odd for replicas.",
        "input_description": "An integer.",
        "expected_output_description": "Even port OR Odd port",
        "starter_code": "# Read port number, print Even or Odd\n",
        "tags": ["operators", "modulo", "conditionals"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "8080", "expected_output": "Even port", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "8443", "expected_output": "Odd port", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `% 2` to check even/odd: `port % 2 == 0` means even.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Modulo operator %", "explanation": "The `%` operator returns the remainder of division. `n % 2 == 0` means n is even. `n % 2 == 1` means odd.", "code_example": "port = 8080\nif port % 2 == 0:\n    print('Even port')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Replica Count Calculator",
        "problem_statement": "Read total requests per second and max requests per pod. Print the minimum number of pods needed (round UP).",
        "scenario": "Kubernetes HPA scaling decisions: compute minimum replicas needed to handle load.",
        "input_description": "Line 1: total_rps (int). Line 2: max_rps_per_pod (int).",
        "expected_output_description": "Pods needed: <number>",
        "starter_code": "import math\n# Read total_rps and max_rps_per_pod, print pods needed\n",
        "tags": ["arithmetic", "math", "devops"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": ["math"], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "1000\n300", "expected_output": "Pods needed: 4", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "500\n100", "expected_output": "Pods needed: 5", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "1001\n500", "expected_output": "Pods needed: 3", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `math.ceil(total / per_pod)` to round up.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "math.ceil() for rounding up", "explanation": "`math.ceil(x)` rounds x up to the next integer. Essential when computing minimum resource counts — you can never have a fraction of a pod.", "code_example": "import math\npods = math.ceil(1000 / 300)  # 4\nprint(f'Pods needed: {pods}')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Environment Variable Simulation",
        "problem_statement": "Simulate reading environment variables by reading key=value pairs from input.\nRead one line in format KEY=VALUE. Print:\nKey: KEY\nValue: VALUE",
        "scenario": "Ops scripts parse env vars constantly. This simulates extracting values from KEY=VALUE format.",
        "input_description": "A string like 'DATABASE_URL=postgres://localhost/db'",
        "expected_output_description": "Key: DATABASE_URL\nValue: postgres://localhost/db",
        "starter_code": "# Read KEY=VALUE and split on first '='\n",
        "tags": ["strings", "split", "env-vars"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "DATABASE_URL=postgres://localhost/db", "expected_output": "Key: DATABASE_URL\nValue: postgres://localhost/db", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "API_KEY=abc123=extra", "expected_output": "Key: API_KEY\nValue: abc123=extra", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `.split('=', 1)` to split only on the FIRST '=' sign.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "split with maxsplit argument", "explanation": "`.split(sep, maxsplit)` limits how many splits occur. `.split('=', 1)` splits on only the first `=`, preserving any `=` in the value.", "code_example": "line = 'KEY=val=ue'\nkey, value = line.split('=', 1)\nprint(key)   # KEY\nprint(value) # val=ue", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Ternary Operator for Status",
        "problem_statement": "Read a CPU usage percentage (0-100). Print 'CRITICAL' if >= 90, else 'NORMAL'. Use a single-line conditional expression.",
        "scenario": "Alert scripts need concise threshold checks. Practice Python's ternary expression.",
        "input_description": "An integer 0-100.",
        "expected_output_description": "CRITICAL or NORMAL",
        "starter_code": "# Read CPU%, print CRITICAL or NORMAL using ternary expression\n",
        "tags": ["conditionals", "ternary"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "95", "expected_output": "CRITICAL", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "70", "expected_output": "NORMAL", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "90", "expected_output": "CRITICAL", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Python ternary: `'CRITICAL' if cpu >= 90 else 'NORMAL'`", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Ternary/conditional expression", "explanation": "Python's ternary: `value_if_true if condition else value_if_false`. Concise for simple conditional assignments.", "code_example": "cpu = int(input())\nstatus = 'CRITICAL' if cpu >= 90 else 'NORMAL'\nprint(status)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "String Repetition Banner",
        "problem_statement": "Read a title string. Print it surrounded by '=' characters on its own line, with a separator of 40 '=' chars above and below.\nExample for 'Deployment Report':\n========================================\nDeployment Report\n========================================",
        "scenario": "Script output headers make long log files easier to scan.",
        "input_description": "A string.",
        "expected_output_description": "40 '=' chars, then title, then 40 '=' chars.",
        "starter_code": "# Read title and print with separator lines\n",
        "tags": ["strings", "repetition", "formatting"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "Deployment Report", "expected_output": "========================================\nDeployment Report\n========================================", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use string repetition: `'=' * 40`", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "String repetition operator *", "explanation": "`string * n` repeats the string n times: `'=' * 40` gives 40 equal signs. Useful for generating banners and separators.", "code_example": "sep = '=' * 40\nprint(sep)\nprint(title)\nprint(sep)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Multi-line String Operations",
        "problem_statement": "Read a multi-word hostname (like 'web server 01') and:\n1. Replace spaces with hyphens\n2. Convert to lowercase\n3. Print the result",
        "scenario": "Hostname normalization: standardize input from users into valid DNS-safe hostnames.",
        "input_description": "A string that may contain spaces.",
        "expected_output_description": "web-server-01 (lowercased, spaces → hyphens)",
        "starter_code": "# Normalize hostname\n",
        "tags": ["strings", "replace", "lower"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "Web Server 01", "expected_output": "web-server-01", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "Database Primary Node", "expected_output": "database-primary-node", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Chain methods: `input().lower().replace(' ', '-')`", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Method chaining on strings", "explanation": "String methods return new strings, so you can chain them: `s.lower().replace(' ', '-').strip()`. This is very common in data normalization functions.", "code_example": "host = input().lower().replace(' ', '-')\nprint(host)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Padding Port Display",
        "problem_statement": "Read a port number. Print it right-aligned in a field of 6 characters, padded with spaces.\nExample: 80 → '    80'\nExample: 8080 → '  8080'",
        "scenario": "Network config display in tabular format requires consistent column widths.",
        "input_description": "An integer.",
        "expected_output_description": "Port right-aligned to 6 chars.",
        "starter_code": "# Read port and print right-aligned to 6 chars\n",
        "tags": ["string-formatting", "alignment"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "80", "expected_output": "    80", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "8080", "expected_output": "  8080", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "443", "expected_output": "   443", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use f-string with width: `f'{port:>6}'` or `str(port).rjust(6)`", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Formatting alignment with f-strings", "explanation": "`f'{value:>N}'` right-aligns value in N chars. `<` for left, `^` for center. Works for both integers and strings.", "code_example": "port = 80\nprint(f'{port:>6}')  # '    80'", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Concurrent Requests Load Check",
        "problem_statement": "Read max_concurrent_requests and max_per_worker. Print:\nWorkers needed (ceil division): <n>\nSurplus capacity: <max_per_worker * workers - max_concurrent_requests>",
        "scenario": "Nginx worker process sizing: compute how many workers needed and spare capacity.",
        "input_description": "Line 1: max_concurrent. Line 2: max_per_worker.",
        "expected_output_description": "Workers needed: 4\nSurplus capacity: 200",
        "starter_code": "import math\n# Calculate workers needed and surplus\n",
        "tags": ["arithmetic", "math", "devops"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": ["math"], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "1000\n300", "expected_output": "Workers needed: 4\nSurplus capacity: 200", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "500\n250", "expected_output": "Workers needed: 2\nSurplus capacity: 0", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "workers = math.ceil(max_concurrent / max_per_worker)\nsurplus = workers * max_per_worker - max_concurrent", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Ceiling division and surplus", "explanation": "When dividing resources, always round up with `math.ceil()`. Surplus = allocated - needed. This pattern applies to pods, workers, threads.", "code_example": "import math\nworkers = math.ceil(1000 / 300)  # 4\nsurplus = 4 * 300 - 1000  # 200", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Time Estimation for Deployment",
        "problem_statement": "Read number of services and time_per_service in seconds. Compute total time.\nPrint:\nTotal time: Xm Ys\nWhere X is minutes and Y is remaining seconds.",
        "scenario": "Deployment pipelines display estimated total deploy time based on service count.",
        "input_description": "Line 1: services count (int). Line 2: seconds per service (int).",
        "expected_output_description": "Total time: 5m 0s",
        "starter_code": "# Calculate total deploy time in minutes and seconds\n",
        "tags": ["arithmetic", "time", "formatting"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "10\n30", "expected_output": "Total time: 5m 0s", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "7\n45", "expected_output": "Total time: 5m 15s", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "total_secs = services * time_per_service\nminutes = total_secs // 60\nseconds = total_secs % 60", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Time decomposition with // and %", "explanation": "Convert seconds to minutes and remaining seconds using `//` and `%`. This pattern is universal for time display in scripts.", "code_example": "total = 315\nminutes = total // 60  # 5\nseconds = total % 60   # 15", "unlocks_after_failures": 3},
        ],
    },
]
