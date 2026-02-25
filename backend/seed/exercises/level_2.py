"""
Level 2: Control Flow — 20 exercises
Topics: if/elif/else, logical operators, loops, break/continue
"""

LEVEL_2_EXERCISES = [
    {
        "title": "Port Range Validator",
        "problem_statement": "Read a port number. Print:\n'Valid user port' if 1024-65535\n'Well-known port' if 1-1023\n'Invalid port' otherwise",
        "scenario": "Port validation prevents misconfigured services from starting on reserved ports.",
        "input_description": "Integer port number.",
        "expected_output_description": "Valid user port / Well-known port / Invalid port",
        "starter_code": "# Validate port range\n",
        "tags": ["conditionals", "if-elif-else", "devops"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "8080", "expected_output": "Valid user port", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "80", "expected_output": "Well-known port", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "0", "expected_output": "Invalid port", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "70000", "expected_output": "Invalid port", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use if/elif/else with range checks.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Check 1–1023 first, then 1024–65535, then else.", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "if/elif/else chains", "explanation": "Use `if/elif/else` for mutually exclusive conditions. Python checks conditions in order — the first True branch runs. Order matters when ranges overlap.", "code_example": "port = int(input())\nif 1 <= port <= 1023:\n    print('Well-known')\nelif 1024 <= port <= 65535:\n    print('Valid user port')\nelse:\n    print('Invalid')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Retry Simulation",
        "problem_statement": "Simulate 5 retry attempts. Print 'Attempt N: failed' for N=1,2,3,4 and 'Attempt 5: success' for the last one.",
        "scenario": "Retry logic is fundamental in distributed system scripts — services may be temporarily unavailable.",
        "input_description": "No input.",
        "expected_output_description": "Attempt 1: failed\nAttempt 2: failed\nAttempt 3: failed\nAttempt 4: failed\nAttempt 5: success",
        "starter_code": "# Simulate 5 retry attempts\n",
        "tags": ["loops", "for-loop", "devops"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "Attempt 1: failed\nAttempt 2: failed\nAttempt 3: failed\nAttempt 4: failed\nAttempt 5: success", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `for i in range(1, 6):` to loop from 1 to 5.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Check `if i == 5:` to print success for the last attempt.", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "for loop with range()", "explanation": "`range(1, 6)` generates 1,2,3,4,5. Combine with `if i == last:` to handle the final iteration differently.", "code_example": "for i in range(1, 6):\n    if i == 5:\n        print(f'Attempt {i}: success')\n    else:\n        print(f'Attempt {i}: failed')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Password Strength Checker",
        "problem_statement": "Read a password. Print its strength:\n'Weak' if length < 8\n'Medium' if 8-11 chars\n'Strong' if >= 12 chars AND contains a digit\n'Medium' if >= 12 but no digit",
        "scenario": "DevOps automation tools generate and validate secrets. A basic strength checker is a common utility.",
        "input_description": "A password string.",
        "expected_output_description": "Weak / Medium / Strong",
        "starter_code": "# Evaluate password strength\n",
        "tags": ["conditionals", "strings", "logic"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "abc", "expected_output": "Weak", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "password", "expected_output": "Medium", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "Secr3tP@ssword", "expected_output": "Strong", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "verylongpassword", "expected_output": "Medium", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Check `len(pw) < 8` first. Then check `len(pw) >= 12`.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Use `any(c.isdigit() for c in pw)` to check for digits.", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "any() with generator expression", "explanation": "`any(condition for item in iterable)` returns True if any item satisfies the condition. Efficient and Pythonic for string scanning.", "code_example": "pw = 'Secret123'\nhas_digit = any(c.isdigit() for c in pw)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "CPU Threshold Alert",
        "problem_statement": "Read 5 CPU usage values (one per line). Print 'ALERT: CPU spike on reading N' for any value >= 85. Print 'All clear' at the end if no alerts fired, otherwise print 'Monitoring complete'.",
        "scenario": "Continuous monitoring loop: check 5 consecutive CPU readings and alert on spikes.",
        "input_description": "5 integers, one per line.",
        "expected_output_description": "ALERT lines for spikes, then 'All clear' or 'Monitoring complete'",
        "starter_code": "# Read 5 CPU readings, alert on spikes\n",
        "tags": ["loops", "conditionals", "monitoring"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "70\n80\n90\n65\n88", "expected_output": "ALERT: CPU spike on reading 3\nALERT: CPU spike on reading 5\nMonitoring complete", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "60\n70\n55\n65\n40", "expected_output": "All clear", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use a flag variable `alerted = False`. Set to True when an alert fires.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Flag variables in loops", "explanation": "A flag (boolean variable) tracks whether something happened inside a loop. Set it True when the event occurs, check it after the loop to decide final output.", "code_example": "alerted = False\nfor i in range(1, 6):\n    val = int(input())\n    if val >= 85:\n        print(f'ALERT: spike on reading {i}')\n        alerted = True\nprint('Monitoring complete' if alerted else 'All clear')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Countdown Timer",
        "problem_statement": "Read a number N. Print countdown from N to 1, then print 'Deploy!'",
        "scenario": "Deployment countdowns give operators a chance to abort before launch.",
        "input_description": "A positive integer N.",
        "expected_output_description": "3\n2\n1\nDeploy!",
        "starter_code": "# Print countdown from N to 1, then Deploy!\n",
        "tags": ["loops", "range", "devops"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "3", "expected_output": "3\n2\n1\nDeploy!", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "5", "expected_output": "5\n4\n3\n2\n1\nDeploy!", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `range(N, 0, -1)` to count down.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "range() with step -1", "explanation": "`range(start, stop, step)` with negative step counts down. `range(5, 0, -1)` gives 5,4,3,2,1.", "code_example": "for i in range(5, 0, -1):\n    print(i)\nprint('Deploy!')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Log Level Filter",
        "problem_statement": "Read N (number of log lines), then N lines of format 'LEVEL message'.\nPrint only ERROR and CRITICAL lines.",
        "scenario": "Log filtering scripts extract only high-severity lines for incident response.",
        "input_description": "First line: count N. Then N lines each starting with INFO/WARN/ERROR/CRITICAL.",
        "expected_output_description": "Only ERROR and CRITICAL lines printed.",
        "starter_code": "# Filter and print only ERROR/CRITICAL log lines\n",
        "tags": ["loops", "strings", "filtering", "logs"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "4\nINFO service started\nWARN high memory\nERROR disk full\nCRITICAL db down", "expected_output": "ERROR disk full\nCRITICAL db down", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "2\nINFO all good\nINFO deployment done", "expected_output": "", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Read N then loop N times. Check if line starts with 'ERROR' or 'CRITICAL'.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "String startswith() for filtering", "explanation": "`.startswith()` checks the beginning of a string. Combined with `if`, it's the core of log filtering scripts.", "code_example": "n = int(input())\nfor _ in range(n):\n    line = input()\n    if line.startswith('ERROR') or line.startswith('CRITICAL'):\n        print(line)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "FizzBuzz DevOps Edition",
        "problem_statement": "Print numbers 1 to 20. Replace:\n- Multiples of 3 → 'Deploy'\n- Multiples of 5 → 'Scale'\n- Multiples of both → 'DeployScale'",
        "scenario": "A classic logic exercise reframed for DevOps terminology — tests your loop and conditional logic.",
        "input_description": "No input.",
        "expected_output_description": "1\n2\nDeploy\n4\nScale\nDeploy\n...",
        "starter_code": "# FizzBuzz DevOps edition 1-20\n",
        "tags": ["loops", "modulo", "conditionals"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "1\n2\nDeploy\n4\nScale\nDeploy\n7\n8\nDeploy\nScale\n11\nDeploy\n13\n14\nDeployScale\n16\n17\nDeploy\n19\nScale", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Check divisible by BOTH first (15), then individually.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Order of conditions matters", "explanation": "In FizzBuzz-style problems, always check the combined condition first. If you check divisible-by-3 first, you'll miss the combined case.", "code_example": "for i in range(1, 21):\n    if i % 15 == 0:\n        print('DeployScale')\n    elif i % 3 == 0:\n        print('Deploy')\n    elif i % 5 == 0:\n        print('Scale')\n    else:\n        print(i)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "break on Error Detection",
        "problem_statement": "Read log lines until you see one containing 'FATAL'. Print each line until (not including) FATAL. Print 'Fatal error found. Stopping.' at the end.\nIf no FATAL found after all lines, print 'Log scan complete. No fatal errors.'",
        "scenario": "Real log scanners stop processing at fatal errors to prevent cascading analysis on corrupted logs.",
        "input_description": "Read lines until empty line (signals end of input).",
        "expected_output_description": "Lines before FATAL, then stopping message.",
        "starter_code": "# Scan log lines, break on FATAL\nimport sys\nlines = sys.stdin.read().splitlines()\n# Process lines\n",
        "tags": ["loops", "break", "logs"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": ["sys"], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "INFO starting\nWARN low mem\nFATAL crash\nINFO recovery", "expected_output": "INFO starting\nWARN low mem\nFatal error found. Stopping.", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "INFO step 1\nINFO step 2", "expected_output": "INFO step 1\nINFO step 2\nLog scan complete. No fatal errors.", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use a `for` loop with `break`. Track if FATAL was found with a flag.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "break and for/else", "explanation": "Python's `for/else`: the `else` block runs ONLY if the loop completed without `break`. Perfect for 'found/not-found' patterns.", "code_example": "for line in lines:\n    if 'FATAL' in line:\n        print('Fatal found')\n        break\n    print(line)\nelse:\n    print('No fatal errors')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Skip DEBUG Lines (continue)",
        "problem_statement": "Read N log lines. Print all lines EXCEPT those starting with 'DEBUG'.",
        "scenario": "Debug logs are noisy in production. Scripts filter them out before forwarding to log aggregators.",
        "input_description": "First line: N. Then N log lines.",
        "expected_output_description": "All lines except DEBUG lines.",
        "starter_code": "# Skip DEBUG lines using continue\n",
        "tags": ["loops", "continue", "filtering"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "4\nINFO deploy started\nDEBUG loading config\nWARN memory high\nDEBUG vars dumped", "expected_output": "INFO deploy started\nWARN memory high", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `continue` to skip to the next iteration when the line starts with DEBUG.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "continue skips current iteration", "explanation": "`continue` immediately jumps to the next loop iteration, skipping the rest of the current one. Use it to filter items in a loop.", "code_example": "for line in lines:\n    if line.startswith('DEBUG'):\n        continue\n    print(line)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "While Loop Health Check",
        "problem_statement": "Simulate a health check that retries until healthy.\nRead health values one per line (OK or FAIL) until OK is received. Print:\n'Check N: FAIL' for failures\n'Check N: OK - Service healthy!' when OK",
        "scenario": "Kubernetes readiness probe simulation: keep checking until service reports OK.",
        "input_description": "Lines of 'OK' or 'FAIL' (guaranteed to get OK eventually).",
        "expected_output_description": "Check 1: FAIL\nCheck 2: FAIL\nCheck 3: OK - Service healthy!",
        "starter_code": "import sys\nlines = sys.stdin.read().splitlines()\n# Use while loop to simulate health check\n",
        "tags": ["while-loop", "devops", "health-check"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": ["sys"], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "FAIL\nFAIL\nOK", "expected_output": "Check 1: FAIL\nCheck 2: FAIL\nCheck 3: OK - Service healthy!", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "OK", "expected_output": "Check 1: OK - Service healthy!", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use a while loop with a counter. Check each line with an if.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "while loops for retry logic", "explanation": "`while` loops are ideal for polling/retry patterns where you don't know how many iterations are needed. They run until the condition is False.", "code_example": "i = 0\nwhile True:\n    status = read_next()\n    i += 1\n    if status == 'OK':\n        print(f'Check {i}: OK')\n        break\n    print(f'Check {i}: FAIL')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Logical Operators: Access Control",
        "problem_statement": "Read username and role (two lines). Grant access if:\n- role is 'admin', OR\n- role is 'ops' AND username starts with 'sre-'\nOtherwise deny. Print 'Access granted' or 'Access denied'.",
        "scenario": "RBAC (Role-Based Access Control) logic appears in every auth middleware script.",
        "input_description": "Line 1: username. Line 2: role.",
        "expected_output_description": "Access granted / Access denied",
        "starter_code": "# Implement access control logic\n",
        "tags": ["logical-operators", "conditionals", "security"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "alice\nadmin", "expected_output": "Access granted", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "sre-bob\nops", "expected_output": "Access granted", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "bob\nops", "expected_output": "Access denied", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "charlie\ndev", "expected_output": "Access denied", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Combine conditions: `if role == 'admin' or (role == 'ops' and username.startswith('sre-')):`", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "and/or logical operators", "explanation": "`and` requires both sides True. `or` requires at least one True. Use parentheses to group: `(A and B) or C`.", "code_example": "if role == 'admin' or (role == 'ops' and user.startswith('sre-')):\n    print('Access granted')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Sum Until Threshold",
        "problem_statement": "Read integers one per line until you hit 0 (sentinel). Print the running total and stop when adding a value would exceed 1000. Print 'Limit reached' if stopped early, else 'Done' with total.",
        "scenario": "Batch processing scripts often cap total payload size to prevent memory issues.",
        "input_description": "Integers one per line, terminated by 0.",
        "expected_output_description": "Total: <n> then Limit reached or Done",
        "starter_code": "import sys\nlines = sys.stdin.read().splitlines()\n# Sum values with threshold check\n",
        "tags": ["while-loop", "break", "accumulation"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": ["sys"], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "200\n400\n300\n500\n0", "expected_output": "Total: 900\nLimit reached", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "100\n200\n300\n0", "expected_output": "Total: 600\nDone", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Accumulate in a total variable. Check `if total + val > 1000: break`", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Sentinel-based loops with accumulation", "explanation": "A sentinel value (like 0) signals end of input. Check the threshold before adding each value to decide whether to stop early.", "code_example": "total = 0\nfor line in lines:\n    val = int(line)\n    if val == 0:\n        break\n    if total + val > 1000:\n        print('Limit reached')\n        break\n    total += val", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Nested Loop: Server Grid",
        "problem_statement": "Print a grid of server names for 3 datacenters (dc1, dc2, dc3) and 3 nodes each (node1, node2, node3):\ndc1-node1\ndc1-node2\n...dc3-node3",
        "scenario": "Infrastructure inventory generation using nested loops for datacenter × node combinations.",
        "input_description": "No input.",
        "expected_output_description": "9 lines: dc1-node1 through dc3-node3",
        "starter_code": "# Generate server grid with nested loops\n",
        "tags": ["nested-loops", "string-formatting"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "dc1-node1\ndc1-node2\ndc1-node3\ndc2-node1\ndc2-node2\ndc2-node3\ndc3-node1\ndc3-node2\ndc3-node3", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Two nested `for` loops: outer for dc (1-3), inner for node (1-3).", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Nested for loops", "explanation": "Nested `for` loops iterate over every combination of two ranges. Outer loop runs once, inner loop runs fully for each outer iteration.", "code_example": "for dc in range(1, 4):\n    for node in range(1, 4):\n        print(f'dc{dc}-node{node}')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Number Guessing: Bisection Logic",
        "problem_statement": "Simulate bisection guessing: given a target number (read from input), start at 50. Each round: if guess < target print 'Too low', guess higher; if guess > target print 'Too high', guess lower; if equal print 'Found: N in K attempts'. Use midpoint bisection (integer). Max 10 attempts.",
        "scenario": "Binary search thinking is essential for efficient log scanning and sorted-array operations.",
        "input_description": "An integer 1-100.",
        "expected_output_description": "Too low/Too high lines, then Found: N in K attempts",
        "starter_code": "target = int(input())\nlow, high = 1, 100\n# Implement bisection search simulation\n",
        "tags": ["while-loop", "bisection", "algorithms"],
        "difficulty": "hard", "xp_reward": 20, "allowed_imports": [], "timeout_secs": 5,
        "test_cases": [
            {"input_data": "50", "expected_output": "Found: 50 in 1 attempts", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "75", "expected_output": "Too low\nFound: 75 in 2 attempts", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Start with low=1, high=100. Each round: guess = (low+high)//2", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Update: if guess < target: low = guess + 1\nif guess > target: high = guess - 1", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "Binary search / bisection", "explanation": "Bisection halves the search space each round. It finds a value in at most log2(N) steps. This is how `bisect` module and sorted lookups work.", "code_example": "low, high = 1, 100\nattempts = 0\nwhile low <= high:\n    mid = (low + high) // 2\n    attempts += 1\n    if mid == target:\n        print(f'Found: {mid} in {attempts} attempts')\n        break\n    elif mid < target:\n        low = mid + 1\n    else:\n        high = mid - 1", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Mock Log Entry Generator",
        "problem_statement": "Read N. Generate N log entries with timestamps starting at 00:00:01 incrementing by 1 second:\n[00:00:01] INFO Service check 1\n[00:00:02] INFO Service check 2\n...",
        "scenario": "Testing log parsers requires generating synthetic log data in exact format.",
        "input_description": "Integer N (number of log lines to generate).",
        "expected_output_description": "N log lines with incrementing timestamps.",
        "starter_code": "# Generate N mock log entries with timestamps\n",
        "tags": ["loops", "string-formatting", "time"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "3", "expected_output": "[00:00:01] INFO Service check 1\n[00:00:02] INFO Service check 2\n[00:00:03] INFO Service check 3", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "1", "expected_output": "[00:00:01] INFO Service check 1", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `range(1, n+1)`. Format seconds as HH:MM:SS using `//` and `%`.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "f'{secs//3600:02d}:{(secs%3600)//60:02d}:{secs%60:02d}'", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "Zero-padded time formatting", "explanation": "`:02d` in f-strings pads integers to 2 digits with leading zeros. `{5:02d}` → `05`. Essential for timestamp generation.", "code_example": "for i in range(1, n+1):\n    ts = f'00:00:{i:02d}'\n    print(f'[{ts}] INFO Service check {i}')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "IP Validation (Format Check)",
        "problem_statement": "Read an IP string. Validate it has exactly 4 parts separated by dots, each part is an integer 0-255. Print 'Valid IP' or 'Invalid IP'.",
        "scenario": "Config validators check network inputs before they hit your infrastructure.",
        "input_description": "A string to validate as IP.",
        "expected_output_description": "Valid IP / Invalid IP",
        "starter_code": "# Validate IPv4 address format\n",
        "tags": ["strings", "validation", "loops", "networking"],
        "difficulty": "hard", "xp_reward": 20, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "192.168.1.1", "expected_output": "Valid IP", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "256.1.1.1", "expected_output": "Invalid IP", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "192.168.1", "expected_output": "Invalid IP", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "not.an.ip.addr", "expected_output": "Invalid IP", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Split on '.', check length == 4, then check each part is integer 0-255.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Use try/except to handle non-integer parts: `int(part)` may raise ValueError.", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "Input validation pattern", "explanation": "Validation = split + count check + type check + range check. Use try/except around `int()` to handle non-numeric input gracefully.", "code_example": "parts = ip.split('.')\nif len(parts) != 4:\n    print('Invalid IP')\n    exit()\nfor p in parts:\n    if not p.isdigit() or not 0 <= int(p) <= 255:\n        print('Invalid IP')\n        exit()\nprint('Valid IP')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Fibonacci for Backoff",
        "problem_statement": "Print the first N Fibonacci numbers (starting 1, 1, 2, 3, 5...). These represent exponential backoff wait times in seconds.",
        "scenario": "Exponential backoff in retry logic uses Fibonacci or powers-of-2. Generate the sequence.",
        "input_description": "Integer N.",
        "expected_output_description": "N Fibonacci numbers, one per line.",
        "starter_code": "# Print first N Fibonacci numbers\n",
        "tags": ["loops", "fibonacci", "algorithms"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "6", "expected_output": "1\n1\n2\n3\n5\n8", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "1", "expected_output": "1", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "10", "expected_output": "1\n1\n2\n3\n5\n8\n13\n21\n34\n55", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Start with a=1, b=1. Each step: print a, then a, b = b, a+b", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Fibonacci with tuple swap", "explanation": "Track two variables a and b. Each round: print a, then update both with `a, b = b, a+b`. No third variable needed.", "code_example": "a, b = 1, 1\nfor _ in range(n):\n    print(a)\n    a, b = b, a + b", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Environment Selection",
        "problem_statement": "Read an environment name. Use if/elif to print the matching config:\n- prod → DB: prod-db.internal Port: 5432\n- staging → DB: staging-db.internal Port: 5433\n- dev → DB: localhost Port: 5434\n- anything else → Unknown environment",
        "scenario": "Environment-specific config loading is a core pattern in deployment scripts.",
        "input_description": "Environment name string.",
        "expected_output_description": "DB and Port lines for the matched environment.",
        "starter_code": "# Print environment-specific config\n",
        "tags": ["if-elif", "config", "devops"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "prod", "expected_output": "DB: prod-db.internal\nPort: 5432", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "staging", "expected_output": "DB: staging-db.internal\nPort: 5433", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "dev", "expected_output": "DB: localhost\nPort: 5434", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "test", "expected_output": "Unknown environment", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use if/elif/elif/else for each environment.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Multi-branch if/elif", "explanation": "Each `elif` adds another branch to check. The `else` is a catch-all. This is the Python equivalent of a switch statement.", "code_example": "env = input()\nif env == 'prod':\n    print('DB: prod-db.internal')\nelif env == 'staging':\n    print('DB: staging-db.internal')\nelse:\n    print('Unknown environment')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Service Health Batch Check",
        "problem_statement": "Read N service names and their statuses (two per line, space separated). Count and print:\nHealthy: X\nUnhealthy: Y\nList all unhealthy services, one per line.",
        "scenario": "Platform health summaries aggregate service statuses for operator dashboards.",
        "input_description": "First line: N. Then N lines of 'servicename status' (status: UP or DOWN).",
        "expected_output_description": "Healthy: 2\nUnhealthy: 1\nUnhealthy services:\nservice-b",
        "starter_code": "# Read N services, count healthy/unhealthy\n",
        "tags": ["loops", "counting", "lists", "devops"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "3\nservice-a UP\nservice-b DOWN\nservice-c UP", "expected_output": "Healthy: 2\nUnhealthy: 1\nUnhealthy services:\nservice-b", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "2\napigateway UP\nauth-service UP", "expected_output": "Healthy: 2\nUnhealthy: 0\nUnhealthy services:", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Keep a list of unhealthy services and counters for UP/DOWN.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Accumulating into lists while counting", "explanation": "Use separate counters for each category, and a list to track specific items. Print the list after the loop.", "code_example": "unhealthy = []\nfor _ in range(n):\n    name, status = input().split()\n    if status == 'DOWN':\n        unhealthy.append(name)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Threshold Escalation",
        "problem_statement": "Read CPU%, Memory%, Disk% (3 inputs). Print alert level:\n- Any metric >= 90 → CRITICAL\n- Any metric >= 75 → WARNING\n- Otherwise → OK\nPrint the level and which metrics triggered it.",
        "scenario": "Tiered alert systems classify incidents before paging on-call engineers.",
        "input_description": "Three integers on separate lines: cpu, memory, disk.",
        "expected_output_description": "CRITICAL\nTriggered by: CPU, Memory (or similar)",
        "starter_code": "# Read 3 metrics, determine alert level\n",
        "tags": ["conditionals", "logical-operators", "monitoring"],
        "difficulty": "hard", "xp_reward": 20, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "92\n85\n60", "expected_output": "CRITICAL\nTriggered by: CPU", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "70\n78\n65", "expected_output": "WARNING\nTriggered by: Memory", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "50\n60\n70", "expected_output": "OK", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Build lists of which metrics are critical/warning. Use max() to determine overall level.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Multi-metric escalation pattern", "explanation": "Collect violations at each threshold into lists. The highest threshold with any violations determines the alert level.", "code_example": "critical = []\nwarning = []\nif cpu >= 90: critical.append('CPU')\nelif cpu >= 75: warning.append('CPU')\n# ...", "unlocks_after_failures": 3},
        ],
    },
]
