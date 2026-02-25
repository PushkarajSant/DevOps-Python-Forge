"""
Level 3: Data Structures — 25 exercises
Topics: Lists, Tuples, Sets, Dictionaries, Nested data handling
"""

LEVEL_3_EXERCISES = [
    {
        "title": "Server List Operations",
        "problem_statement": "Given a list of servers: ['web-01', 'web-02', 'db-01', 'cache-01', 'web-03']\nPrint:\n1. Total servers\n2. First server\n3. Last server\n4. All web servers (starting with 'web'), one per line",
        "scenario": "Inventory scripts enumerate and filter server lists from discovered hosts.",
        "input_description": "No input.",
        "expected_output_description": "5\nweb-01\nweb-03\nweb-01\nweb-02\nweb-03",
        "starter_code": "servers = ['web-01', 'web-02', 'db-01', 'cache-01', 'web-03']\n# Print stats and filtered list\n",
        "tags": ["lists", "filtering", "indexing"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "5\nweb-01\nweb-03\nweb-01\nweb-02\nweb-03", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use len(), servers[0], servers[-1], and a list comprehension with startswith().", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "List indexing and filtering", "explanation": "Lists support `len()`, `[0]` (first), `[-1]` (last), and comprehensions: `[s for s in lst if condition]`.", "code_example": "web = [s for s in servers if s.startswith('web')]\nfor s in web:\n    print(s)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Remove Duplicate IPs",
        "problem_statement": "Read N IP addresses (one per line). Print unique IPs in the order they first appeared.",
        "scenario": "Log files contain repeated IPs. Deduplication is essential before IP reputation lookups.",
        "input_description": "First line: N. Then N IP strings.",
        "expected_output_description": "Unique IPs, first-seen order.",
        "starter_code": "# Deduplicate IPs preserving order\n",
        "tags": ["sets", "lists", "deduplication"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "5\n192.168.1.1\n10.0.0.1\n192.168.1.1\n10.0.0.2\n10.0.0.1", "expected_output": "192.168.1.1\n10.0.0.1\n10.0.0.2", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use a set `seen` and a list `result`. Add to result only if not already in seen.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Set for O(1) lookup, list for order", "explanation": "Sets give fast `in` checks but don't preserve order. Use both: a set to track seen items, a list to preserve insertion order.", "code_example": "seen = set()\nresult = []\nfor ip in ips:\n    if ip not in seen:\n        seen.add(ip)\n        result.append(ip)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Count HTTP Status Codes",
        "problem_statement": "Read N log lines like 'GET /path 200'. Count occurrences of each status code.\nPrint each code and count sorted by code numerically:\n200: 3\n404: 1\n500: 2",
        "scenario": "Access log analysis: counting error codes reveals service health at a glance.",
        "input_description": "First line: N. Then N log lines.",
        "expected_output_description": "status_code: count, sorted numerically.",
        "starter_code": "# Count HTTP status codes from log lines\n",
        "tags": ["dictionaries", "counting", "logs"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "5\nGET /home 200\nGET /api 500\nPOST /login 200\nGET /missing 404\nGET /home 200", "expected_output": "200: 3\n404: 1\n500: 1", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use a dict `counts = {}`. For each line, split and get the last part (status code).", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "counts[code] = counts.get(code, 0) + 1", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "dict.get() for counting", "explanation": "`dict.get(key, default)` returns default if key missing — perfect for counting without KeyError. Sort by key with `sorted(dict.items())`.", "code_example": "counts = {}\nfor line in lines:\n    code = line.split()[-1]\n    counts[code] = counts.get(code, 0) + 1\nfor k in sorted(counts):\n    print(f'{k}: {counts[k]}')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Parse Config Dictionary",
        "problem_statement": "Given the config dict below, print each key-value pair sorted alphabetically by key:\ndatabase=postgres\nhost=localhost\nport=5432\ntimeout=30",
        "scenario": "Config introspection: print all settings for audit or debugging.",
        "input_description": "No input.",
        "expected_output_description": "database=postgres\nhost=localhost\nport=5432\ntimeout=30",
        "starter_code": "config = {\n    'host': 'localhost',\n    'port': 5432,\n    'database': 'postgres',\n    'timeout': 30\n}\n# Print sorted key=value pairs\n",
        "tags": ["dictionaries", "iteration", "sorting"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "database=postgres\nhost=localhost\nport=5432\ntimeout=30", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `sorted(config.items())` to iterate in alphabetical order.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Iterating dicts with items()", "explanation": "`dict.items()` returns key-value pairs. Use `sorted()` to iterate in sorted key order.", "code_example": "for k, v in sorted(config.items()):\n    print(f'{k}={v}')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Merge Configuration Dicts",
        "problem_statement": "Merge two config dicts: defaults are overridden by overrides.\nDefaults: {'timeout': 30, 'retries': 3, 'debug': False}\nOverrides: {'timeout': 60, 'loglevel': 'INFO'}\nPrint merged result sorted by key as key=value.",
        "scenario": "Layer-based config merging is used in Kubernetes, Ansible, and Helm for environment overrides.",
        "input_description": "No input.",
        "expected_output_description": "debug=False\nloglevel=INFO\nretries=3\ntimeout=60",
        "starter_code": "defaults = {'timeout': 30, 'retries': 3, 'debug': False}\noverrides = {'timeout': 60, 'loglevel': 'INFO'}\n# Merge and print\n",
        "tags": ["dictionaries", "merge", "config"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "debug=False\nloglevel=INFO\nretries=3\ntimeout=60", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `merged = {**defaults, **overrides}` — overrides' keys win.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Dict merging with **unpacking", "explanation": "`{**dict1, **dict2}` creates a new dict combining both. If a key exists in both, the second dict's value wins (override pattern).", "code_example": "merged = {**defaults, **overrides}\nfor k, v in sorted(merged.items()):\n    print(f'{k}={v}')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Extract IPs from JSON-like Structure",
        "problem_statement": "Given a nested dict of services (hardcoded), extract all IP values and print them sorted.\nservices = {'web': {'ip': '10.0.0.1', 'port': 80}, 'db': {'ip': '10.0.0.2', 'port': 5432}, 'cache': {'ip': '10.0.0.3', 'port': 6379}}",
        "scenario": "Service discovery: extract all IPs from a service registry response.",
        "input_description": "No input.",
        "expected_output_description": "10.0.0.1\n10.0.0.2\n10.0.0.3",
        "starter_code": "services = {\n    'web': {'ip': '10.0.0.1', 'port': 80},\n    'db': {'ip': '10.0.0.2', 'port': 5432},\n    'cache': {'ip': '10.0.0.3', 'port': 6379}\n}\n# Extract and print all IPs sorted\n",
        "tags": ["nested-dict", "extraction", "devops"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "10.0.0.1\n10.0.0.2\n10.0.0.3", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Iterate `services.values()` → each is a dict with 'ip' key.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Navigating nested dicts", "explanation": "Access nested values with chained keys: `d['outer']['inner']`. Use `dict.values()` to iterate all values.", "code_example": "ips = sorted([s['ip'] for s in services.values()])\nfor ip in ips:\n    print(ip)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Tuple Immutability Check",
        "problem_statement": "Create a tuple of environment names: ('dev', 'staging', 'prod'). Print:\n1. Number of environments\n2. Whether 'prod' is in the tuple\n3. Index of 'staging'\n4. A new tuple with 'dr' appended",
        "scenario": "Immutable environment lists prevent accidental modification in shared scripts.",
        "input_description": "No input.",
        "expected_output_description": "3\nTrue\n1\n('dev', 'staging', 'prod', 'dr')",
        "starter_code": "envs = ('dev', 'staging', 'prod')\n# Print tuple stats and extended tuple\n",
        "tags": ["tuples", "immutability"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "3\nTrue\n1\n('dev', 'staging', 'prod', 'dr')", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use len(), 'prod' in envs, .index(), and tuple concatenation: envs + ('dr',)", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Tuples: immutable sequences", "explanation": "Tuples are immutable lists. They support `len()`, `in`, `.index()`, but not `.append()`. To 'add' an element, create a new tuple: `t + (new_item,)`.", "code_example": "envs = ('dev', 'staging', 'prod')\nnew = envs + ('dr',)\nprint(new)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Set Operations: Common Hosts",
        "problem_statement": "Find servers that are in BOTH active_servers and monitored_servers.\nactive = {'web-01', 'web-02', 'db-01', 'cache-01'}\nmonitored = {'web-01', 'db-01', 'backup-01', 'cache-02'}\nPrint common servers sorted alphabetically, one per line.",
        "scenario": "Identifying hosts missing from monitoring coverage requires set intersection.",
        "input_description": "No input.",
        "expected_output_description": "db-01\nweb-01",
        "starter_code": "active = {'web-01', 'web-02', 'db-01', 'cache-01'}\nmonitored = {'web-01', 'db-01', 'backup-01', 'cache-02'}\n# Find and print common servers\n",
        "tags": ["sets", "intersection", "devops"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "db-01\nweb-01", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `active & monitored` or `active.intersection(monitored)` for set intersection.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Set intersection with &", "explanation": "`set1 & set2` returns elements in BOTH sets. `set1 | set2` = union. `set1 - set2` = difference (in set1 but not set2).", "code_example": "common = active & monitored\nfor s in sorted(common):\n    print(s)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Unmonitored Servers",
        "problem_statement": "Using the same sets from the previous exercise, find servers that are active but NOT monitored. Print sorted.",
        "scenario": "Active servers missing from monitoring are a coverage gap — immediate security risk.",
        "input_description": "No input.",
        "expected_output_description": "cache-01\nweb-02",
        "starter_code": "active = {'web-01', 'web-02', 'db-01', 'cache-01'}\nmonitored = {'web-01', 'db-01', 'backup-01', 'cache-02'}\n# Find active but NOT monitored servers\n",
        "tags": ["sets", "difference", "devops"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "cache-01\nweb-02", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `active - monitored` for set difference.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Set difference", "explanation": "`set1 - set2` gives elements in set1 that are NOT in set2. The monitoring gap pattern: `active - monitored`.", "code_example": "gap = active - monitored\nfor s in sorted(gap):\n    print(s)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "List Comprehension: Filter Ports",
        "problem_statement": "Given a list of ports: [21, 22, 80, 443, 3306, 5432, 6379, 8080, 8443, 27017]\nUse a list comprehension to extract only ports > 1024. Print them space-separated on one line.",
        "scenario": "Network audits filter non-standard ports for security review.",
        "input_description": "No input.",
        "expected_output_description": "3306 5432 6379 8080 8443 27017",
        "starter_code": "ports = [21, 22, 80, 443, 3306, 5432, 6379, 8080, 8443, 27017]\n# Filter ports > 1024 with list comprehension\n",
        "tags": ["lists", "list-comprehension", "filtering"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "3306 5432 6379 8080 8443 27017", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "filtered = [p for p in ports if p > 1024]\nThen print with `' '.join(map(str, filtered))`", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "List comprehension syntax", "explanation": "`[expression for item in iterable if condition]` — creates a new list from filtered/transformed items in one concise line.", "code_example": "high_ports = [p for p in ports if p > 1024]\nprint(' '.join(map(str, high_ports)))", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "env Var Processor",
        "problem_statement": "Read N lines of KEY=VALUE env vars. Build a dict. Then print:\n1. All keys sorted\n2. Value of 'DATABASE_URL' (or 'NOT SET' if missing)\n3. Count of keys containing 'DB'",
        "scenario": "CI/CD scripts parse environment variables from .env files for validation.",
        "input_description": "First line: N. Then N KEY=VALUE lines.",
        "expected_output_description": "Sorted keys, DATABASE_URL value, DB key count.",
        "starter_code": "# Parse N env vars and analyze\n",
        "tags": ["dictionaries", "env-vars", "parsing"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "3\nDATABASE_URL=postgres://localhost/prod\nDB_POOL=10\nAPP_SECRET=abc123", "expected_output": "APP_SECRET\nDB_POOL\nDATABASE_URL\npostgres://localhost/prod\n2", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "2\nAPP_NAME=forge\nREDIS_URL=redis://localhost", "expected_output": "APP_NAME\nREDIS_URL\nNOT SET\n0", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Parse each line with `.split('=', 1)` into key, value pair.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Building dicts from structured input", "explanation": "Parse each line, split on delimiter, add to dict. Then query the dict for specific keys and filter keys by value.", "code_example": "env = {}\nfor _ in range(n):\n    k, v = input().split('=', 1)\n    env[k] = v\nprint(env.get('DATABASE_URL', 'NOT SET'))", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Kubernetes Pod Status Counter",
        "problem_statement": "Read N pod status lines like 'pod-name Running'. Count pods by status and print:\nRunning: X\nPending: Y\nFailed: Z\n(Print only statuses that appear, sorted alphabetically)",
        "scenario": "kubectl output parsing: summarize pod counts by status for operators.",
        "input_description": "First line: N. Then N lines of 'pod-name Status'.",
        "expected_output_description": "Status: count, sorted.",
        "starter_code": "# Count k8s pod statuses\n",
        "tags": ["dictionaries", "counting", "kubernetes"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "5\npod-1 Running\npod-2 Running\npod-3 Pending\npod-4 Running\npod-5 Failed", "expected_output": "Failed: 1\nPending: 1\nRunning: 3", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use a dict with `counts.get(status, 0) + 1`. Sort with `sorted(counts.items())`.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Frequency counting with dicts", "explanation": "The pattern: `d[key] = d.get(key, 0) + 1` counts occurrences. This is equivalent to `collections.Counter` but without imports.", "code_example": "counts = {}\nfor line in lines:\n    _, status = line.split()\n    counts[status] = counts.get(status, 0) + 1", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Slicing for Log Tail",
        "problem_statement": "Read N log lines. Print only the last 5 lines (or all if fewer than 5). This simulates `tail -5`.",
        "scenario": "`tail` is one of the most used log commands. Implement it in Python using list slicing.",
        "input_description": "First line: N. Then N log lines.",
        "expected_output_description": "Last min(5, N) lines.",
        "starter_code": "# Simulate tail -5 using list slicing\nimport sys\nlines = sys.stdin.read().splitlines()\n",
        "tags": ["lists", "slicing", "logs"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": ["sys"], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "7\nline1\nline2\nline3\nline4\nline5\nline6\nline7", "expected_output": "line3\nline4\nline5\nline6\nline7", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "3\nonly-1\nonly-2\nonly-3", "expected_output": "only-1\nonly-2\nonly-3", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "After reading N (first line), use `lines[1:][-5:]` to get data lines and tail 5.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Negative slicing with [-n:]", "explanation": "`list[-5:]` gives the last 5 elements safely (returns all if fewer than 5). This is how `tail` works conceptually.", "code_example": "data = lines[1:]  # skip count line\nfor line in data[-5:]:\n    print(line)", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Nested Config Access",
        "problem_statement": "Given nested config, print all database connection details:\nconfig = {'app': {'name': 'forge', 'version': '1.0'}, 'database': {'host': 'db.prod.internal', 'port': 5432, 'name': 'forge_db', 'credentials': {'user': 'admin', 'pass': 'secret'}}}\nPrint: host, port, db name, user (not password).",
        "scenario": "Config parsers safely extract specific values from deeply nested structures.",
        "input_description": "No input.",
        "expected_output_description": "Host: db.prod.internal\nPort: 5432\nDB: forge_db\nUser: admin",
        "starter_code": "config = {\n    'app': {'name': 'forge', 'version': '1.0'},\n    'database': {\n        'host': 'db.prod.internal',\n        'port': 5432,\n        'name': 'forge_db',\n        'credentials': {'user': 'admin', 'pass': 'secret'}\n    }\n}\n# Extract and print DB connection details\n",
        "tags": ["nested-dict", "config", "devops"],
        "difficulty": "easy", "xp_reward": 10, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "Host: db.prod.internal\nPort: 5432\nDB: forge_db\nUser: admin", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Access with config['database']['host'], then config['database']['credentials']['user']", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Deep nested dict access", "explanation": "Chain `[]` operators: `d['level1']['level2']['level3']`. Add error handling with `.get()` to avoid KeyError on missing keys.", "code_example": "db = config['database']\nprint(f\"Host: {db['host']}\")\nprint(f\"User: {db['credentials']['user']}\")", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Sorted Server Inventory",
        "problem_statement": "Read N servers — name and cpu_count (space separated). Sort by CPU count descending, then by name alphabetically for ties. Print as 'name: Ncpu'.",
        "scenario": "Scheduling workloads on highest-capacity servers requires sorted server inventory.",
        "input_description": "First line: N. Then 'name cpus' lines.",
        "expected_output_description": "Servers sorted by CPU desc, name asc for ties.",
        "starter_code": "# Read servers, sort by cpu desc then name asc\n",
        "tags": ["lists", "sorting", "tuples"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "4\nweb-01 8\ndb-01 16\nweb-02 8\ncache-01 4", "expected_output": "db-01: 16cpu\nweb-01: 8cpu\nweb-02: 8cpu\ncache-01: 4cpu", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Sort with key=lambda x: (-x[1], x[0]) — negative cpu for descending.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Multi-key sorting with lambda", "explanation": "Pass `key=lambda item: (-item[1], item[0])` to `sorted()`. Negate numeric values for descending sort without `reverse=True` conflicting with other keys.", "code_example": "servers = [('web', 8), ('db', 16)]\nsorted_list = sorted(servers, key=lambda x: (-x[1], x[0]))", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Max/Min Request Times",
        "problem_statement": "Read N response times in ms. Print:\nMin: Xms\nMax: Xms\nAvg: X.XXms\nP95 (95th percentile — round to nearest): Xms",
        "scenario": "API performance analysis: latency statistics are critical for SLA monitoring.",
        "input_description": "First line: N. Then N integers.",
        "expected_output_description": "Min, Max, Avg to 2dp, P95.",
        "starter_code": "# Compute latency stats\n",
        "tags": ["lists", "statistics", "devops"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "5\n100\n200\n150\n300\n250", "expected_output": "Min: 100ms\nMax: 300ms\nAvg: 200.00ms\nP95: 300ms", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Sort the list. P95 index = int(0.95 * len(times)). Use min(), max(), sum()/len().", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Percentile calculation", "explanation": "Sort the list. The p-th percentile is at index `int(p/100 * len(data))`. Always clamp to valid index range.", "code_example": "times.sort()\np95_idx = int(0.95 * len(times))\np95 = times[min(p95_idx, len(times)-1)]", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "List of Dicts: Services Inventory",
        "problem_statement": "Given a list of service dicts, print only services where 'status'=='UP' and 'port' > 1024, sorted by port:\nFormat: service_name (port PORT)",
        "scenario": "Service registry filtering: find active non-privileged services for load balancer config.",
        "input_description": "No input.",
        "expected_output_description": "Filtered and sorted services.",
        "starter_code": "services = [\n    {'name': 'api', 'port': 8080, 'status': 'UP'},\n    {'name': 'ssh', 'port': 22, 'status': 'UP'},\n    {'name': 'db', 'port': 5432, 'status': 'DOWN'},\n    {'name': 'cache', 'port': 6379, 'status': 'UP'},\n    {'name': 'metrics', 'port': 9090, 'status': 'UP'},\n]\n# Filter and print\n",
        "tags": ["list-of-dicts", "filtering", "sorting"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "api (port 8080)\ncache (port 6379)\nmetrics (port 9090)", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Filter with list comprehension: `[s for s in services if s['status']=='UP' and s['port']>1024]`\nSort with `sorted(..., key=lambda s: s['port'])`", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Filtering list of dicts", "explanation": "List comprehensions work on lists of dicts: `[s for s in services if s['field'] == val]`. Combine with `sorted()` for full power.", "code_example": "filtered = [s for s in services if s['status']=='UP' and s['port']>1024]\nfor s in sorted(filtered, key=lambda x: x['port']):\n    print(f\"{s['name']} (port {s['port']})\")", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Group Servers by Role",
        "problem_statement": "Read N lines of 'hostname role'. Group by role and print each role with its servers sorted:\ndb: db-01, db-02\nweb: web-01, web-02, web-03",
        "scenario": "Infrastructure grouping helps orchestration tools apply role-specific playbooks.",
        "input_description": "First line: N. Then 'hostname role' lines.",
        "expected_output_description": "Roles sorted, servers within each role sorted.",
        "starter_code": "# Group servers by role into a dict\n",
        "tags": ["dictionaries", "grouping", "lists"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "5\nweb-01 web\ndb-01 db\nweb-02 web\ndb-02 db\nweb-03 web", "expected_output": "db: db-01, db-02\nweb: web-01, web-02, web-03", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use `groups.setdefault(role, []).append(host)` to group.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "setdefault() for grouping", "explanation": "`dict.setdefault(key, [])` returns the value for key (creating an empty list if missing). Perfect for building grouped lists.", "code_example": "groups = {}\nfor line in lines:\n    host, role = line.split()\n    groups.setdefault(role, []).append(host)\nfor role in sorted(groups):\n    print(f\"{role}: {', '.join(sorted(groups[role]))}\")", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Stack for Bracket Matching",
        "problem_statement": "Read a config string containing brackets ([], {}, ()). Use a list as a stack to check if brackets are properly balanced.\nPrint 'Balanced' or 'Unbalanced'.",
        "scenario": "YAML/JSON config validators check for balanced delimiters before parsing.",
        "input_description": "A string.",
        "expected_output_description": "Balanced / Unbalanced",
        "starter_code": "# Use list as stack to check bracket balance\ns = input()\n",
        "tags": ["lists", "stack", "algorithms"],
        "difficulty": "hard", "xp_reward": 20, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "{[()]}", "expected_output": "Balanced", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "{[}", "expected_output": "Unbalanced", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "((()))", "expected_output": "Balanced", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Push opening brackets onto a stack (list). When you see a closing bracket, pop and check if it matches.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Use a dict: `pairs = {')':'(', ']':'[', '}':'{'}`", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "List as stack (LIFO)", "explanation": "A Python list works as a stack: `.append()` pushes, `.pop()` pulls from the end (LIFO). Bracket matching is the classic stack algorithm.", "code_example": "stack = []\npairs = {')':'(', ']':'[', '}':'{'}\nfor c in s:\n    if c in '([{':\n        stack.append(c)\n    elif c in ')]}':\n        if not stack or stack[-1] != pairs[c]:\n            print('Unbalanced')\n            exit()\n        stack.pop()\nprint('Balanced' if not stack else 'Unbalanced')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Queue Simulation for Job Processing",
        "problem_statement": "Simulate a job queue using a list. Read N jobs (add to queue). Process jobs one by one — print 'Processing: job_name' for each. If job starts with 'URGENT:', process it immediately (skip queue).\nPrint queue in order processed.",
        "scenario": "Job schedulers prioritize urgent tasks (like alerts) over normal background jobs.",
        "input_description": "First line: N. Then N job names.",
        "expected_output_description": "Processing lines, urgent jobs first.",
        "starter_code": "import sys\nlines = sys.stdin.read().splitlines()\n# Simulate priority job queue\n",
        "tags": ["lists", "queue", "algorithms"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": ["sys"], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "4\nbackup-db\nURGENT:alert-pagerduty\nrun-tests\nURGENT:scale-up", "expected_output": "Processing: URGENT:alert-pagerduty\nProcessing: URGENT:scale-up\nProcessing: backup-db\nProcessing: run-tests", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Split jobs into urgent and normal lists. Process urgent first.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Priority queues with list partitioning", "explanation": "Simple priority: separate items into buckets by priority. Process high-priority bucket first. For more complex needs, use `heapq`.", "code_example": "urgent = [j for j in jobs if j.startswith('URGENT:')]\nnormal = [j for j in jobs if not j.startswith('URGENT:')]\nfor j in urgent + normal:\n    print(f'Processing: {j}')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "dict.items() Inversion",
        "problem_statement": "Given a port-to-service mapping, invert it (service → port) and print sorted by service name:\nport_map = {22: 'ssh', 80: 'http', 443: 'https', 3306: 'mysql', 5432: 'postgres'}",
        "scenario": "Reverse lookups (service name → port) are common in firewall rule generation scripts.",
        "input_description": "No input.",
        "expected_output_description": "http: 80\nhttps: 443\nmysql: 3306\npostgres: 5432\nssh: 22",
        "starter_code": "port_map = {22: 'ssh', 80: 'http', 443: 'https', 3306: 'mysql', 5432: 'postgres'}\n# Invert the mapping and print sorted\n",
        "tags": ["dictionaries", "inversion"],
        "difficulty": "medium", "xp_reward": 15, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "", "expected_output": "http: 80\nhttps: 443\nmysql: 3306\npostgres: 5432\nssh: 22", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "inverted = {v: k for k, v in port_map.items()}", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Dict comprehension for inversion", "explanation": "`{v: k for k, v in d.items()}` swaps keys and values. Assumes values are unique (no collisions).", "code_example": "inverted = {v: k for k, v in port_map.items()}\nfor svc in sorted(inverted):\n    print(f'{svc}: {inverted[svc]}')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Two-Sum for Capacity Planning",
        "problem_statement": "You have N servers with given capacities (integers). Find and print all PAIRS of servers (by index) whose combined capacity equals a target.\nFormat: (i, j) where i < j",
        "scenario": "Capacity pairing: find two servers whose combined RAM meets a workload requirement.",
        "input_description": "First line: target. Second line: N. Then N integers.",
        "expected_output_description": "(i, j) pairs, one per line, ascending by i.",
        "starter_code": "# Find pairs summing to target\n",
        "tags": ["lists", "algorithms", "two-sum"],
        "difficulty": "hard", "xp_reward": 20, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "16\n5\n8 4 12 6 10", "expected_output": "(0, 2)\n(1, 4)", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "10\n4\n5 5 5 5", "expected_output": "(0, 1)\n(0, 2)\n(0, 3)\n(1, 2)\n(1, 3)\n(2, 3)", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use nested loops: outer i from 0..n-1, inner j from i+1..n.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Nested loop pair enumeration", "explanation": "To find all pairs without duplicates: outer loop i from 0 to n-1, inner loop j from i+1 to n. This covers every pair exactly once.", "code_example": "for i in range(len(caps)):\n    for j in range(i+1, len(caps)):\n        if caps[i] + caps[j] == target:\n            print(f'({i}, {j})')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Rolling Average Monitor",
        "problem_statement": "Read N readings. Print the ROLLING AVERAGE of the last 3 readings at each step (from reading 3 onwards). Before 3 readings: print 'Collecting...'",
        "scenario": "Sliding window averages smooth out spikes in real-time metric dashboards.",
        "input_description": "First line: N. Then N numbers.",
        "expected_output_description": "Collecting...\nCollecting...\nAvg: X.XX per rolling window.",
        "starter_code": "# Compute rolling 3-window average\n",
        "tags": ["lists", "slicing", "statistics"],
        "difficulty": "hard", "xp_reward": 20, "allowed_imports": [], "timeout_secs": 3,
        "test_cases": [
            {"input_data": "5\n100\n200\n150\n300\n250", "expected_output": "Collecting...\nCollecting...\nAvg: 150.00\nAvg: 216.67\nAvg: 233.33", "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Keep readings in a list. For each new reading, check if we have >= 3. If yes, average the last 3.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Rolling window with list[-n:]", "explanation": "At each step, take the slice `readings[-3:]` to get the last 3 items. Average them. This is the sliding window pattern.", "code_example": "readings = []\nfor _ in range(n):\n    readings.append(float(input()))\n    if len(readings) < 3:\n        print('Collecting...')\n    else:\n        avg = sum(readings[-3:]) / 3\n        print(f'Avg: {avg:.2f}')", "unlocks_after_failures": 3},
        ],
    },
]
