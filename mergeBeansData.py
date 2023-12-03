# This script will:

# Load and normalize the data from 'static_data.json' and 'dynamic_data.json'.
# Merge the data based on the FlavorName.
# Keep track of and display items from both datasets that do not find a match.
# Save the merged data to 'merged_beans_data.json'.

import json

# Function to load JSON data from a file
def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Function to save JSON data to a file
def save_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Normalize a string (e.g., FlavorName)
def normalize(name):
    return name.strip().upper()

# Load data from both JSON files
static_data = load_json('static_data.json')
dynamic_data = load_json('dynamic_data.json')

# Normalize the FlavorName in both datasets
for item in static_data:
    item['FlavorName'] = normalize(item['FlavorName'])

for item in dynamic_data:
    item['FlavorName'] = normalize(item['FlavorName'])

# Merge data and track unmatched items
merged_data = []
unmatched_static = []
unmatched_dynamic = {item['FlavorName']: item for item in dynamic_data}

for static_item in static_data:
    flavor_name = static_item['FlavorName']
    dynamic_item = unmatched_dynamic.pop(flavor_name, None)

    if dynamic_item:
        merged_item = {**static_item, **dynamic_item}
        merged_item['GlutenFree'] = False
        merged_item['SugarFree'] = False
        merged_item['Seasonal'] = False
        merged_item['Kosher'] = False
        merged_data.append(merged_item)
    else:
        unmatched_static.append(static_item)

# Save unmatched items to separate JSON files
save_json(unmatched_static, 'unmatched_static_data.json')
save_json(list(unmatched_dynamic.values()), 'unmatched_dynamic_data.json')

# Save the merged data to a new JSON file
save_json(merged_data, 'merged_beans_data.json')

print("Merged data saved to 'merged_beans_data.json'")
print("Unmatched static data saved to 'unmatched_static_data.json'")
print("Unmatched dynamic data saved to 'unmatched_dynamic_data.json'")
