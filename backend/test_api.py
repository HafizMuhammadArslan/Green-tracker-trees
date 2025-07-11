import requests

BASE = "http://127.0.0.1:5000"

# Add new tree 
new_tree = {
    "name": "Test Tree",
    "location": "Test Garden",
    "date": "2025-07-03",
    "status": "Healthy"
}
res = requests.post(f"{BASE}/api/trees", json=new_tree)
print("CREATE:", res.json())

# GET all trees 
res = requests.get(f"{BASE}/api/trees")
trees = res.json()
print("GET:", trees)

# Extract the last added tree ID 
created_id = trees[-1]["id"]

# UPDATE that tree 
update_data = {
    "name": "Updated Tree",
    "location": "Updated Location",
    "date": "2025-08-01",
    "status": "Growing"
}
res = requests.put(f"{BASE}/api/trees/{created_id}", json=update_data)
print("UPDATE:", res.json())

# DELETE that same tree 
res = requests.delete(f"{BASE}/api/trees/{created_id}")
print("DELETE:", res.json())