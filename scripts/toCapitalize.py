import json

# Read the original JSON file
with open('merged_beans_data.json', 'r') as file:
    data = json.load(file)

# Convert the first letter of each word to uppercase for specific keys
def to_capitalized(obj):
    keys_to_capitalize = ["GroupName", "FlavorName", "Description", "Ingredients"]
    
    if isinstance(obj, dict):
        return {k: to_capitalized(v) if k not in keys_to_capitalize else v.title() for k, v in obj.items()}
    elif isinstance(obj, list):
        return [to_capitalized(element) for element in obj]
    elif isinstance(obj, str):
        return obj  # If it's a string not within our targeted keys, leave it as is
    else:
        return obj

capitalized_data = to_capitalized(data)

# Write the capitalized data to a new file
with open('toCapitalize.json', 'w') as file:
    json.dump(capitalized_data, file, indent=4)
