import json
import requests

json_url = "https://github.com/Brolloks/CNC-Members/blob/main/cnc-alliance-members-registration"

response = requests.get(json_url)
print(response.text)
data = json.loads(response.text)

pool_ids = []
for member in data["adapools"]["members"]:
    pool_ids.append(member["poolId"])

with open("pool_ids.json", "w") as outfile:
    json.dump(pool_ids, outfile)

print("Pool IDs successfully written to pool_ids.json")
print(response.text)
