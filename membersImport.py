import json
import requests

json_url = "https://raw.githubusercontent.com/Brolloks/CNC-Members/main/cnc-alliance-members-registration"

response = requests.get(json_url)
print("version 1.1")
data = json.loads(response.text)

pool_ids = []
seen_pool_ids = set()
for key in data["adapools"]["members"].keys():
    v = data["adapools"]["members"][key]
    if v["membershipType?"] in ["Active", "ISPO"]:
        if v["poolId"] in seen_pool_ids:
            pool_ids.append({"ticker" : v["ticker"] + " DUPLICATE", "poolId" : v["poolId"]})
        else:
            pool_ids.append({"ticker" : v["ticker"], "poolId" : v["poolId"]})
            seen_pool_ids.add(v["poolId"])
       
pool_ids = sorted(pool_ids, key = lambda x : x["ticker"])

with open("CNC_Active_ISPO_POOL_CHECK.json", "w") as outfile:
    json.dump(pool_ids, outfile, indent = 2)

print("Pool IDs successfully written to CNC_Active_ISPO_POOL_CHECK.json")
