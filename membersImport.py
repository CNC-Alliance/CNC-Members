import json
import requests

json_url = "https://raw.githubusercontent.com/Brolloks/CNC-Members/main/cnc-alliance-members-registration"

response = requests.get(json_url)
print(response.text)
print("version 1")
data = json.loads(response.text)

pool_ids = []
for key in data["adapools"]["members"].keys():
    v = data["adapools"]["members"][key]
    if v["membershipType"] in ["Active", "ISPO"]:
        pool_ids.append({"ticker" = v["ticker"], "poolId" = v["poolId"]})
       
pool_ids = sorted(pool_ids, key = lambda x : x["ticker"])

with open("pool_ids.json", "w") as outfile:
    json.dump(pool_ids, outfile)

print("Pool IDs successfully written to pool_ids.json")
print(response.text)
