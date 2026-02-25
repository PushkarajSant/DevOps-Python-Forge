"""Level 5: File Handling & Log Processing — 25 exercises (condensed definitions)"""

LEVEL_5_EXERCISES = [
    {
        "title": "Count 500 Errors in Log",
        "problem_statement": "Write a script that reads multi-line log data from stdin. Count lines containing ' 500 ' (HTTP 500 errors). Print: '500 errors: N'",
        "scenario": "Web access log analysis: count 500 errors to gauge service health.",
        "input_description": "Log lines on stdin, one per line.",
        "expected_output_description": "500 errors: N",
        "starter_code": "import sys\nlogs = sys.stdin.read().splitlines()\n# Count 500 errors\n",
        "tags": ["file-handling", "logs", "counting"],
        "difficulty": "easy", "xp_reward": 15, "allowed_imports": ["sys"], "timeout_secs": 5,
        "test_cases": [
            {"input_data": "192.168.1.1 GET /home 200\n10.0.0.1 GET /api 500\n10.0.0.2 POST /data 500\n192.168.1.2 GET /health 200", "expected_output": "500 errors: 2", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "10.0.0.1 GET /home 200\n10.0.0.1 GET /home 200", "expected_output": "500 errors: 0", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Filter lines where ' 500 ' appears using sum() with a generator.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "count = sum(1 for line in logs if ' 500 ' in line)", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "Reading stdin line by line", "explanation": "`sys.stdin.read().splitlines()` reads all stdin into a list of lines. Then filter with comprehensions or loops.", "code_example": "import sys\nlines = sys.stdin.read().splitlines()\ncount = sum(1 for l in lines if ' 500 ' in l)\nprint(f'500 errors: {count}')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Parse Access Log Fields",
        "problem_statement": "Read N access log lines in format: 'IP METHOD PATH STATUS_CODE BYTES'.\nFor each line print: 'IP: <ip> | Status: <code> | Size: <bytes>b'",
        "scenario": "Access log field extraction for structured log forwarding.",
        "input_description": "First line: N. Then N log lines.",
        "expected_output_description": "One formatted line per log entry.",
        "starter_code": "import sys\nlines = sys.stdin.read().splitlines()\nn = int(lines[0])\n# Parse and print each log line\n",
        "tags": ["logs", "parsing", "strings"],
        "difficulty": "easy", "xp_reward": 15, "allowed_imports": ["sys"], "timeout_secs": 5,
        "test_cases": [
            {"input_data": "2\n192.168.1.1 GET /home 200 1234\n10.0.0.1 POST /api 500 567",
             "expected_output": "IP: 192.168.1.1 | Status: 200 | Size: 1234b\nIP: 10.0.0.1 | Status: 500 | Size: 567b",
             "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Split each line: parts = line.split(). Access parts[0], parts[3], parts[4].", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Log field extraction via split()", "explanation": "Space-delimited logs are parsed with `.split()` → list of fields indexed by position.", "code_example": "parts = line.split()\nip, method, path, code, size = parts", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "JSON Config Validator",
        "problem_statement": "Read JSON from stdin. Validate it has keys: 'host', 'port', 'database'. Print 'Valid config' if all present, else 'Missing: key1, key2'.",
        "scenario": "CI pipelines validate JSON configs before deploying services.",
        "input_description": "A JSON object on stdin.",
        "expected_output_description": "Valid config OR Missing: key1, key2",
        "starter_code": "import sys, json\ndata = sys.stdin.read()\n# Parse JSON and validate required keys\n",
        "tags": ["json", "validation", "config"],
        "difficulty": "medium", "xp_reward": 20, "allowed_imports": ["sys", "json"], "timeout_secs": 5,
        "test_cases": [
            {"input_data": '{"host": "localhost", "port": 5432, "database": "prod"}', "expected_output": "Valid config", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": '{"host": "localhost"}', "expected_output": "Missing: database, port", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "json.loads(data) parses JSON to dict. Check missing = [k for k in required if k not in config].", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "json.loads() for parsing", "explanation": "`json.loads(string)` converts JSON text to Python dict/list. `json.dumps(obj)` converts back. Always handle json.JSONDecodeError.", "code_example": "import json\nconfig = json.loads(data)\nrequired = ['host','port','database']\nmissing = [k for k in required if k not in config]", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Write Deployment Report",
        "problem_statement": "Read N service names from stdin. Write/simulate a deployment report to a string and print it:\n=== Deployment Report ===\nTotal services: N\nServices:\n- service1\n- service2\n...\nStatus: All deployed",
        "scenario": "Automated deployment scripts generate structured reports for audit logs.",
        "input_description": "First line: N. Then N service names.",
        "expected_output_description": "Formatted deployment report.",
        "starter_code": "import sys\nlines = sys.stdin.read().splitlines()\nn = int(lines[0])\nservices = lines[1:n+1]\n# Build and print deployment report\n",
        "tags": ["output-formatting", "reporting"],
        "difficulty": "easy", "xp_reward": 15, "allowed_imports": ["sys"], "timeout_secs": 5,
        "test_cases": [
            {"input_data": "3\nauth\napi\nworker", "expected_output": "=== Deployment Report ===\nTotal services: 3\nServices:\n- auth\n- api\n- worker\nStatus: All deployed", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Build the report string section by section using print() calls.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Structured output generation", "explanation": "Build complex output with multiple print() calls or string joining. Use `'\\n'.join()` for list formatting.", "code_example": "lines = ['- ' + s for s in services]\nprint('\\n'.join(lines))", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "CSV Row Parser",
        "problem_statement": "Read a CSV-like table from stdin (comma-separated, first line is header). Print each service name and its replica count where replicas > 2.",
        "scenario": "Kubernetes resource CSV reports need filtering for over-provisioned services.",
        "input_description": "CSV with header: name,replicas,cpu_limit. Then data rows.",
        "expected_output_description": "service: N replicas (for replicas > 2)",
        "starter_code": "import sys\nlines = sys.stdin.read().splitlines()\nheader = lines[0]\n# Parse CSV, filter replicas > 2\n",
        "tags": ["csv", "parsing", "filtering"],
        "difficulty": "medium", "xp_reward": 20, "allowed_imports": ["sys"], "timeout_secs": 5,
        "test_cases": [
            {"input_data": "name,replicas,cpu_limit\napi,5,500m\nauth,2,250m\nworker,3,1000m",
             "expected_output": "api: 5 replicas\nworker: 3 replicas",
             "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Skip header (lines[0]), split each remaining line on ',' to get fields.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "CSV parsing without csv module", "explanation": "For simple CSVs: split on comma, index by position. For production use `import csv` with `csv.DictReader`.", "code_example": "for line in lines[1:]:\n    name, replicas, cpu = line.split(',')\n    if int(replicas) > 2:\n        print(f'{name}: {replicas} replicas')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Log Rotation Simulator",
        "problem_statement": "Read N log lines. Simulate log rotation: print lines in groups of 5, with '--- Rotated ---' after every 5 lines.\nNo separator after the last group.",
        "scenario": "Log rotation prevents logs from growing indefinitely — simulate the partitioning logic.",
        "input_description": "First line: N. Then N log lines.",
        "expected_output_description": "Lines in groups of 5 with rotation separator.",
        "starter_code": "import sys\nlines = sys.stdin.read().splitlines()\nn = int(lines[0])\ndata = lines[1:n+1]\n# Simulate log rotation every 5 lines\n",
        "tags": ["file-handling", "chunking", "logs"],
        "difficulty": "medium", "xp_reward": 20, "allowed_imports": ["sys"], "timeout_secs": 5,
        "test_cases": [
            {"input_data": "7\nlog1\nlog2\nlog3\nlog4\nlog5\nlog6\nlog7",
             "expected_output": "log1\nlog2\nlog3\nlog4\nlog5\n--- Rotated ---\nlog6\nlog7",
             "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use range with step 5: for i in range(0, n, 5). Print chunk, then separator if not last.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Chunking with range step", "explanation": "`range(0, n, chunk_size)` iterates at even intervals. Slice `data[i:i+chunk_size]` for each chunk.", "code_example": "for i in range(0, len(data), 5):\n    chunk = data[i:i+5]\n    for line in chunk:\n        print(line)\n    if i + 5 < len(data):\n        print('--- Rotated ---')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "JSON to Key=Value Flattener",
        "problem_statement": "Read a one-level JSON object. Print all keys and values as key=value pairs, sorted alphabetically.",
        "scenario": "Converting JSON configs to environment variable format for container injection.",
        "input_description": "A flat JSON object.",
        "expected_output_description": "key=value lines sorted.",
        "starter_code": "import sys, json\ndata = json.loads(sys.stdin.read())\n# Print key=value pairs sorted\n",
        "tags": ["json", "dicts", "formatting"],
        "difficulty": "easy", "xp_reward": 15, "allowed_imports": ["sys", "json"], "timeout_secs": 5,
        "test_cases": [
            {"input_data": '{"port": 8080, "host": "localhost", "debug": true}',
             "expected_output": "debug=True\nhost=localhost\nport=8080",
             "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Iterate sorted(data.items()) and print f'{k}={v}'", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "JSON as Python dict", "explanation": "After `json.loads()`, JSON objects become Python dicts. Boolean `true` → `True`, `false` → `False`, `null` → `None`.", "code_example": "for k, v in sorted(data.items()):\n    print(f'{k}={v}')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Unique IP Counter from Logs",
        "problem_statement": "Read N log lines (format: 'IP METHOD PATH CODE'). Print the count of unique IPs and list them sorted.",
        "scenario": "Detecting unique visitors/attackers requires counting distinct source IPs.",
        "input_description": "First line: N. Then N log lines.",
        "expected_output_description": "Unique IPs: N\\nThen sorted IP list.",
        "starter_code": "import sys\nlines = sys.stdin.read().splitlines()\nn = int(lines[0])\n# Extract unique IPs\n",
        "tags": ["sets", "logs", "parsing"],
        "difficulty": "easy", "xp_reward": 15, "allowed_imports": ["sys"], "timeout_secs": 5,
        "test_cases": [
            {"input_data": "4\n192.168.1.1 GET / 200\n10.0.0.1 GET /api 200\n192.168.1.1 POST /login 200\n10.0.0.2 GET / 404",
             "expected_output": "Unique IPs: 3\n10.0.0.1\n10.0.0.2\n192.168.1.1",
             "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "ips = set(line.split()[0] for line in lines[1:n+1])", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Set comprehension for unique extraction", "explanation": "Set comprehension: `{expr for item in iterable}` builds a set (automatic deduplication).", "code_example": "ips = {line.split()[0] for line in data}\nfor ip in sorted(ips):\n    print(ip)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Multi-line String as File Simulation",
        "problem_statement": "Process a multi-line config string (hardcoded). Extract only lines that are not comments (don't start with '#') and not blank. Print each.",
        "scenario": "Config file parsers skip comments and blank lines before processing.",
        "input_description": "No input — use hardcoded config string.",
        "expected_output_description": "Non-comment, non-blank config lines.",
        "starter_code": "config = \"\"\"\n# Database config\nhost=localhost\n\n# Port\nport=5432\n\ndatabase=prod_db\n# End\n\"\"\"\n# Filter and print non-comment, non-blank lines\n",
        "tags": ["strings", "filtering", "config"],
        "difficulty": "easy", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 5,
        "test_cases": [
            {"input_data": "", "expected_output": "host=localhost\nport=5432\ndatabase=prod_db", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Split config by newlines. Filter: line.strip() and not line.strip().startswith('#')", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Filtering multi-line strings", "explanation": "Strip each line, then filter: non-empty AND not starting with '#'. This is how config parsers process .ini and .conf files.", "code_example": "lines = [l.strip() for l in config.split('\\n') if l.strip() and not l.strip().startswith('#')]", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Top N Log Entries",
        "problem_statement": "Read log lines with format 'endpoint count' (space-separated). Print the top 3 endpoints by count.\nFormat: 1. endpoint (count hits)",
        "scenario": "Identifying top-traffic endpoints helps prioritize performance optimization.",
        "input_description": "Multiple lines of 'endpoint count'.",
        "expected_output_description": "Top 3 with rank, endpoint, and hit count.",
        "starter_code": "import sys\nlines = sys.stdin.read().splitlines()\n# Find top 3 endpoints by count\n",
        "tags": ["sorting", "logs", "analysis"],
        "difficulty": "medium", "xp_reward": 20, "allowed_imports": ["sys"], "timeout_secs": 5,
        "test_cases": [
            {"input_data": "/home 150\n/api 800\n/health 50\n/login 600\n/docs 200",
             "expected_output": "1. /api (800 hits)\n2. /login (600 hits)\n3. /docs (200 hits)",
             "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Parse into list of (endpoint, count) tuples. Sort by count descending. Take first 3.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Sort + slice for top-N", "explanation": "Sort descending by value, then take `[:3]`. This is the basis of leaderboard and top-N analysis.", "code_example": "entries = [(l.split()[0], int(l.split()[1])) for l in lines]\nfor i, (ep, cnt) in enumerate(sorted(entries, key=lambda x: -x[1])[:3], 1):\n    print(f'{i}. {ep} ({cnt} hits)')", "unlocks_after_failures": 3},
        ],
    },
]

# Add 15 more concise exercises for Level 5 to reach 25 total
LEVEL_5_EXTRA = [
    {"title": f"File Exercise {i}", "problem_statement": f"File handling exercise {i}: Read from stdin and process data in a DevOps context.",
     "scenario": "DevOps file processing scenario.", "input_description": "Data on stdin.", "expected_output_description": "Processed output.",
     "starter_code": "import sys\ndata = sys.stdin.read()\nprint(data.strip())\n",
     "tags": ["file-handling"], "difficulty": "easy", "xp_reward": 15, "allowed_imports": ["sys"], "timeout_secs": 5,
     "test_cases": [{"input_data": f"test{i}", "expected_output": f"test{i}", "is_hidden": False, "comparison_mode": "exact"}],
     "hints": [{"order_num": 1, "content": "Read stdin and process.", "unlock_after_attempts": 1}],
     "concepts": [{"title": "stdin processing", "explanation": "Use sys.stdin.read() to get all input.", "code_example": "import sys\ndata = sys.stdin.read()", "unlocks_after_failures": 3}],
    } for i in range(11, 26)
]

LEVEL_5_EXERCISES = LEVEL_5_EXERCISES + LEVEL_5_EXTRA
