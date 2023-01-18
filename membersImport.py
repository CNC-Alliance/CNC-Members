import json
import sys

# Load the JSON data from the file
with open(sys.argv[1], 'r') as json_file:
    data = json.load(cnc-alliance-members-registration)

# Create a new list to store the poolIds of the entries that have "Active" or "ISPO" in the membershipType field
pool_ids = []

# Iterate through the entries in the JSON data
for entry in data.values():
    # Check if the entry has "Active" or "ISPO" in the membershipType field
    if entry['membershipType'] in ['Active', 'ISPO']:
        # If so, add the poolId to the list
        pool_ids.append(entry['poolId'])

# Write the list of poolIds to a new JSON file
with open('pool_ids.json', 'w') as json_file:
    json.dump(pool_ids, json_file)
