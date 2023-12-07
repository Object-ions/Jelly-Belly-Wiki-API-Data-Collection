Steps to scrape:

1. Get static data from url using `staticScraper.py`.

This script will scrape the url and collect "static" data and export the output to `staticScraper.json`

url = 'https://www.jellybelly.com/jelly-belly-flavor-collections'

The data includes:

- "Group Name"
- "Flavor Name"
- "Background Color"
- "Image URL"

2. Get "dynamic" data from url using: `dynamicScraper.py`, `getXpathsBtns.py`,

This stage will include a few steps:

A. `getXpathsBtns.py` - Run a script to target all buttons that will trigger the data fetching. Extract the buttons xpath and save the result in `button_xpaths.json`.
B. `dynamicScraper.py` - Run a script to get ChromeDriver click on the coresponding xpaths of the buttons and collect data the includes:

- "FlavorName"
- "Description"
- "Ingredients"
  and will export the output to `dynamic_data.json`.

3. `mergeBeansData.py` - cross information and merge duplicates between files.
   Load and normalize the data from 'static_data.json' and 'dynamic_data.json'. Merge the data based on the FlavorName .Keep track of and display items from both datasets that do not find a match. the data will be exported as follow:
   Merged data saved to `merged_beans_data.json`
   Unmatched static data saved to `unmatched_static_data.json`
   Unmatched dynamic data saved to `unmatched_dynamic_data.json`

4. Manually compare `merged_beans_data.json`, `unmatched_static_data.json`, `unmatched_dynamic_data.json` and extract a final file named `merged_beans_data.json` that will contain 113 objects with this entries:
   "BeanId"
   "GroupName"
   "FlavorName"
   "BackgroundColor"
   "ImageUrl"
   "Description"
   "Ingredients"
   "GlutenFree"
   "SugarFree"
   "Seasonal"
   "Kosher"

5. `toCapitalize.py` - This script will take the file that contain the data and turn it's content capitalized (exclude the entries)

6. `prepToSeed.py` - this script will take the objects in `merged_beans_data.json` and format it to be ready to be seeded as data in the API


