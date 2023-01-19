import json
import os

filepath = os.path.join(os.path.dirname(__file__),"cnc-alliance-members-registration")

with open(filepath) as json_file:
    data = json.load(json_file)

pool_ids = {}

for key, value in data.items():
    if value["membershipType"] in ["Active", "ISPO"]:
        pool_ids[value["ticker"]] = value["poolId"]

with open("pool_ids.json", "w") as outfile:
    json.dump(pool_ids, outfile)
