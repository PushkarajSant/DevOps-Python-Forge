"""Level 7: API & Networking — 20 exercises (core 5 + 15 placeholders)"""

LEVEL_7_EXERCISES = [
    {
        "title": "Parse API JSON Response",
        "problem_statement": "Given a JSON string representing an API response, extract and print:\n- status code\n- number of results\n- first result's 'name' field\nJSON format: {\"status\": 200, \"results\": [{\"name\": \"...\", ...}, ...]}\nRead JSON from stdin.",
        "scenario": "Parsing REST API responses is the core skill for any automation script that integrates with cloud APIs.",
        "input_description": "A JSON string.",
        "expected_output_description": "Status: 200\nResults: N\nFirst: name_value",
        "starter_code": "import sys, json\ndata = json.loads(sys.stdin.read())\n# Extract and print API response fields\n",
        "tags": ["json", "api", "parsing"],
        "difficulty": "medium", "xp_reward": 20, "allowed_imports": ["sys", "json"], "timeout_secs": 5,
        "test_cases": [
            {"input_data": '{"status": 200, "results": [{"name": "web-pod-1", "ready": true}, {"name": "web-pod-2", "ready": false}]}',
             "expected_output": "Status: 200\nResults: 2\nFirst: web-pod-1",
             "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Access: data['status'], len(data['results']), data['results'][0]['name']", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "Navigating JSON API responses", "explanation": "API responses frequently nest data: `response['results'][0]['field']`. Always check `len()` before indexing to avoid IndexError.", "code_example": "status = data['status']\nresults = data['results']\nprint(f'First: {results[0][\"name\"]}')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Simulate HTTP Status Handler",
        "problem_statement": "Read an HTTP status code. Print the appropriate message:\n2xx → 'Success'\n401 → 'Unauthorized: check credentials'\n403 → 'Forbidden: insufficient permissions'\n404 → 'Not Found'\n429 → 'Rate Limited: slow down'\n5xx → 'Server Error: retry later'\nOther → 'Unknown status code'",
        "scenario": "API clients must handle different HTTP status ranges gracefully before retrying or failing.",
        "input_description": "An integer HTTP status code.",
        "expected_output_description": "Status message.",
        "starter_code": "code = int(input())\n# Handle HTTP status codes\n",
        "tags": ["api", "conditionals", "networking"],
        "difficulty": "medium", "xp_reward": 20, "allowed_imports": [], "timeout_secs": 5,
        "test_cases": [
            {"input_data": "200", "expected_output": "Success", "is_hidden": False, "comparison_mode": "exact"},
            {"input_data": "404", "expected_output": "Not Found", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "503", "expected_output": "Server Error: retry later", "is_hidden": True, "comparison_mode": "exact"},
            {"input_data": "429", "expected_output": "Rate Limited: slow down", "is_hidden": True, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Check specific codes first (401, 403, 404, 429), then use 200 <= code < 300 for 2xx, 500 <= code < 600 for 5xx.", "unlock_after_attempts": 1},
        ],
        "concepts": [
            {"title": "HTTP status code ranges", "explanation": "2xx=success, 3xx=redirect, 4xx=client error, 5xx=server error. Check specific codes before ranges.", "code_example": "if code == 404:\n    print('Not Found')\nelif 200 <= code < 300:\n    print('Success')\nelif 500 <= code < 600:\n    print('Server Error: retry later')", "unlocks_after_failures": 3},
        ],
    },
    {
        "title": "Build Query String",
        "problem_statement": "Read N key=value pairs from stdin. Build a URL query string sorted by key: '?key1=val1&key2=val2'. Print the full URL: 'https://api.example.com/v1/pods?key1=val1...'",
        "scenario": "Building API query strings programmatically is required when constructing dynamic requests in scripts.",
        "input_description": "First line: N. Then N key=value lines.",
        "expected_output_description": "Full URL with sorted query string.",
        "starter_code": "import sys\nlines = sys.stdin.read().splitlines()\nn = int(lines[0])\nbase_url = 'https://api.example.com/v1/pods'\n# Build query string from key=value pairs\n",
        "tags": ["api", "strings", "url-building"],
        "difficulty": "medium", "xp_reward": 20, "allowed_imports": ["sys"], "timeout_secs": 5,
        "test_cases": [
            {"input_data": "3\nnamespace=default\nlimit=100\nlabelSelector=app=web",
             "expected_output": "https://api.example.com/v1/pods?labelSelector=app%3Dweb&limit=100&namespace=default",
             "is_hidden": False, "comparison_mode": "exact"},
        ],
        "hints": [
            {"order_num": 1, "content": "Use urllib.parse.urlencode(sorted_dict) to build query string.", "unlock_after_attempts": 1},
            {"order_num": 2, "content": "Parse each line with split('=', 1), build dict, sort, use urlencode.", "unlock_after_attempts": 2},
        ],
        "concepts": [
            {"title": "urllib.parse for URL building", "explanation": "`urllib.parse.urlencode(params)` encodes a dict into a URL query string, handling special characters like `=` → `%3D`.", "code_example": "from urllib.parse import urlencode\nparams = {'namespace': 'default', 'limit': 100}\nquery = urlencode(sorted(params.items()))\nprint(f'{base_url}?{query}')", "unlocks_after_failures": 3},
        ],
    },
]

# Placeholder exercises for levels 7-10 reach target counts
def make_placeholders(level_name, topic, count, start=4, difficulty="medium", xp=20):
    return [
        {"title": f"{level_name} Exercise {i}",
         "problem_statement": f"Advanced {topic} exercise {i}. Solve the DevOps scenario using Python.",
         "scenario": f"Real-world {topic} automation scenario.",
         "input_description": "Input from stdin.",
         "expected_output_description": "Processed output.",
         "starter_code": "data = input()\nprint(data)\n",
         "tags": [topic.lower().replace(" ", "-")],
         "difficulty": difficulty, "xp_reward": xp, "allowed_imports": [], "timeout_secs": 5,
         "test_cases": [{"input_data": f"sample{i}", "expected_output": f"sample{i}", "is_hidden": False, "comparison_mode": "exact"}],
         "hints": [{"order_num": 1, "content": f"Think about {topic} patterns.", "unlock_after_attempts": 1}],
         "concepts": [{"title": f"{topic} concept", "explanation": f"Core {topic} concepts for DevOps automation.", "code_example": "# implement here", "unlocks_after_failures": 3}],
        } for i in range(start, start + count)
    ]

LEVEL_7_EXERCISES = LEVEL_7_EXERCISES + make_placeholders("API", "API & Networking", 17, start=4)
