"""Quick end-to-end API test."""
from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from main import app

client = TestClient(app)

# Register + Login
r = client.post("/api/auth/login", data={"username": "testdev77", "password": "Short1!"})
assert r.status_code == 200
token = r.json()["access_token"]
auth = {"Authorization": f"Bearer {token}"}
print("✓ Login OK")

# Get levels
r = client.get("/api/levels", headers=auth)
assert r.status_code == 200
levels = r.json()
assert len(levels) == 11
print(f"✓ Levels: {len(levels)} retrieved, Level 0 unlocked: {levels[0]['is_unlocked']}")

# Get level 0 exercises
r = client.get("/api/levels/0/exercises", headers=auth)
assert r.status_code == 200
exs = r.json()
print(f"✓ Level 0 exercises: {len(exs)}")
ex1 = exs[0]
print(f"  First: {ex1['title']} ({ex1['difficulty']}, +{ex1['xp_reward']} XP)")

# Get exercise detail
r = client.get(f"/api/exercises/{ex1['id']}", headers=auth)
assert r.status_code == 200
ex = r.json()
print(f"✓ Exercise detail: {len(ex['visible_test_cases'])} visible test cases")

# Submit correct solution (Hello World)
code = "print('Hello, DevOps!')"
r = client.post(f"/api/submissions/{ex1['id']}/submit", json={"code": code}, headers=auth)
assert r.status_code == 200
result = r.json()
passed_count = sum(1 for t in result["test_results"] if t["passed"])
print(f"✓ Submit: passed={result['passed']}, xp_awarded={result['xp_awarded']}, tests={passed_count}/{len(result['test_results'])}")

# Test run endpoint
r = client.post(f"/api/submissions/{ex1['id']}/run", json={"code": "print('test run output')"}, headers=auth)
assert r.status_code == 200
output = r.json()
print(f"✓ Run: stdout='{output['stdout']}', error='{output['error']}'")

# Dashboard
r = client.get("/api/progress/dashboard", headers=auth)
assert r.status_code == 200
dash = r.json()
print(f"✓ Dashboard: user={dash['user']['username']}, xp={dash['user']['total_xp']}")

print("\n🎉 ALL TESTS PASSED")
