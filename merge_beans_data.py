import json

# Function to load JSON data from a file
def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Load data from both JSON files
jelly_belly_flavors = load_json('jelly_belly_flavors.json')
main_results = load_json('main_results_capitalized.json')

# Normalize the FlavorName to uppercase in both datasets for consistency
for item in jelly_belly_flavors:
    item['FlavorName'] = item['FlavorName'].upper()

for item in main_results:
    item['FlavorName'] = item['FlavorName'].upper()

# Merge data based on FlavorName
merged_data = []
bean_id = 1

for jelly_item in jelly_belly_flavors:
    flavor_name = jelly_item['FlavorName']
    # Find the matching item in main_results
    main_item = next((item for item in main_results if item['FlavorName'] == flavor_name), None)
    
    if main_item:
        # Merge the two items, with priority to main_item's fields
        merged_item = {**jelly_item, **main_item}
        # Add additional fields
        merged_item['BeanId'] = bean_id
        merged_item['GlutenFree'] = False
        merged_item['SugarFree'] = False
        merged_item['Seasonal'] = False
        merged_item['Kosher'] = False

        merged_data.append(merged_item)
        bean_id += 1

# Save the merged data to a new JSON file
with open('merged_beans_data.json', 'w') as file:
    json.dump(merged_data, file, indent=4)
