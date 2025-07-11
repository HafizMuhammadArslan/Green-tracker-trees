import requests

BASE = "http://127.0.0.1:5000"

#  Create a new tree
new_tree = {
    "name": "Test Tree",
    "location": "Test Garden",
    "date": "2025-07-03",
    "status": "Healthy"
}

res = requests.post(f"{BASE}/api/trees", json=new_tree)
print("CREATE:", res.json())

#  Get all trees
res = requests.get(f"{BASE}/api/trees")
print("GET:", res.json())

#  Delete last tree (optional for test)
last_tree = res.json()[-1]
tree_id = last_tree["id"]

res = requests.delete(f"{BASE}/api/trees/{tree_id}")
print("DELETE:", res.json())
