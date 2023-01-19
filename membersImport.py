import json
import os

filepath = os.path.join(os.path.dirname(__file__),"cnc-alliance-members-registration")

# Load the JSON data from the file
with open(filepath) as json_file:
    data = json.load(json_file)

# Create a new list to store the poolIds of the entries that have "Active" or "ISPO" in the membershipType field
pool_ids = {}

# Iterate through the entries in the JSON data
for key, value in data.items():
    if value["membershipType"] in ["Active", "ISPO"]:
        pool_ids[value["ticker"]] = value["poolId"]

# Write the list of poolIds to a new JSON file
with open("pool_ids.json", "w") as outfile:
    json.dump(pool_ids, outfile)
