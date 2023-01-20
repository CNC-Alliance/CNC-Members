import json

with open("CNC_Active_ISPO_pool_ids.json", "r") as infile:
    data = json.load(infile)

pool_ids = [d["poolId"] for d in data]

with open("CNC_ISPO_OFFICIAL.json", "w") as outfile:
    json.dump(pool_ids, outfile)

print("CNC_ISPO_OFFICIAL.json created successfully")
