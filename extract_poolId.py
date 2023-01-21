import json

# load the output file from the first script
with open("CNC_Active_ISPO_pool_ids.json", "r") as infile:
    data = json.load(infile)

# extract the poolId
pool_ids = [d["poolId"] for d in data]

# write the poolIds to a new output file
with open("CNC_ISPO_OFFICIAL.json", "w") as outfile:
    json.dump(pool_ids, outfile, indent = 2)

print("Pool IDs successfully written to CNC_ISPO_OFFICIAL.json")
