# This script will take the file that contain the data and turn it to capitalize

import json

# Read the original JSON file
with open('main_results.json', 'r') as file:
    data = json.load(file)

# Convert all string values from uppercase to capitalized, excluding specific keys
def to_capitalized(obj):
    if isinstance(obj, dict):
        return {k: to_capitalized(v) if k != 'FlavorName' else v for k, v in obj.items()}
    elif isinstance(obj, list):
        return [to_capitalized(element) for element in obj]
    elif isinstance(obj, str):
        return obj.title()
    else:
        return obj

capitalized_data = to_capitalized(data)

# Write the capitalized data to a new file
with open('main_results_capitalized.json', 'w') as file:
    json.dump(capitalized_data, file, indent=4)
