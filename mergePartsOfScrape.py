# To accomplish the task of merging the contents of the two JSON files (until_wild_blackberry.json and until_locorice.json), removing duplicates, and adding a sequential BeanId to each entry, here's the approach I'll take:

# Read Data from JSON Files: First, I'll read the contents of both JSON files into Python data structures (likely lists of dictionaries).

# Merge Lists: I'll merge these two lists into one combined list. This step doesn't concern itself with duplicates yet; it just creates a single list containing all entries from both files.

# Remove Duplicates: To remove duplicates, I'll use a strategy that identifies unique entries based on a combination of attributes like FlavorName, Description, and Ingredients. Since duplicates are exact matches, this will effectively filter them out. I'll likely use a set or a dictionary to track seen entries for efficient duplicate removal.

# Add BeanId: After removing duplicates, I'll iterate over the now unique list of bean entries and add a sequential BeanId to each entry. This ID will start from 1 and increment for each bean.

# Write to a New JSON File: Finally, I'll write this processed list (now with unique entries and BeanIds) to a new JSON file.

# This approach ensures that the final JSON file contains a unique list of beans, each with a unique ID, and no information is duplicated between entries.

import json

# Function to read JSON file
def read_json(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

# Function to write JSON file
def write_json(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

# Read data from both JSON files
data_blackberry = read_json('until_wild_blackberry.json')
data_locorice = read_json('until_locorice.json')

# Merge the two lists
combined_data = data_blackberry + data_locorice

# Remove duplicates
unique_data = []
seen = set()
for item in combined_data:
    identifier = (item['FlavorName'], item['Description'], item['Ingredients'])
    if identifier not in seen:
        unique_data.append(item)
        seen.add(identifier)

# Add BeanId to each unique entry
for i, item in enumerate(unique_data, start=1):
    item['BeanId'] = i

# Write the unique data with BeanIds to a new JSON file
write_json(unique_data, 'merged_beans.json')

print("Merged data written to merged_beans.json")
