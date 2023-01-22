import json

with open("CNC_Active_ISPO_POOL_CHECK.json", "r") as infile:
    data = json.load(infile)

pool_ids = []
for member in data:
    pool_ids.append(member["poolId"])

with open("CNC_Alliance.json", "w") as outfile:
    json.dump(pool_ids, outfile, indent = 2)

print("Pool IDs successfully written to CNC_Alliance.json")
