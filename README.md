# Jelly Belly API Data Collection and Processing Workflow

## Overview

This document outlines the workflow used for scraping, processing, and preparing Jelly Belly flavor data for API integration.

## 'Bean' class scraping process:

### 1. Data Collection

#### Static Data Scraping (`staticScraper.py`)

- **Purpose**: Scrapes static data from the Jelly Belly flavor collections webpage.
- **Data Collected**:
  - Group Name
  - Flavor Name
  - Background Color
  - Image URL
- **Output**: Data exported to `static_data.json`.

#### Dynamic Data Scraping (`dynamicScraper.py` & `getXpathsBtns.py`)

- **getXpathsBtns.py**:
  - Identifies and extracts XPath of buttons to trigger data fetching.
  - **Output**: XPaths saved in `get_xpaths_btn.json`.
- **dynamicScraper.py**:
  - Uses the extracted XPaths to control ChromeDriver to click on buttons and scrape dynamic data:
    - Flavor Name
    - Description
    - Ingredients
  - **Input**: Data from `get_xpaths_btn.json`.
  - **Output**: Data exported to `dynamic_data.json`.

### 2. Data Merging and Cleaning

#### Merging Data (`mergeBeansData.py`)

- Normalizes and merges data from `static_data.json` and `dynamic_data.json`.
- Remove duplicates and adding a sequential BeanId to each entry.
- Tracks and exports unmatched items from both datasets.
- **Input**: `static_data.json` and `dynamic_data.json`.
- **Outputs**:
  - Merged data in `merged_beans_data.json`.
  - Unmatched static data in `unmatched_static_data.json`.
  - Unmatched dynamic data in `unmatched_dynamic_data.json`.

### 3. Data Validation

#### Searching for Missing Names (`searchForMissingNames.py`)

note : `beans_name_list.json` - is a copy of `get_xpaths_btn.json` with text modification - isolate bean's name from it's xpath.

- Compares expected flavor list (`beans_name_list.json`) with actual entries in `merged_beans_data.json` (to make sure no information was omitted).
- Identifies and displays missing flavors in terminal.
- **Input**: `beans_name_list.json` and `merged_beans_data.json`.
- **Outputs**: list of 'missing' data identified by flavorName to the terminal.

### 4. Data Formatting

#### Capitalization (`toCapitalize.py`)

- Capitalizes strings in the data, keys to capitalize = "GroupName", "FlavorName", "Description", "Ingredients".
- **Input**: Processed data in `merged_beans_data.json` (after checking no beans are missing).
- **Output**: `toCapitalize.json`.

#### Preparation for API Seeding (`prepDataToSeedWithColor.py`)

- Formats data for seeding into the API.
- Add color information to each bean - the script finds the closest CSS3 color name to a given hex color `backgroundColor`
- **Input**: `toCapitalize.json`.
- **Output**: `seeded_beans_with_color_name.txt`, `list_of_colors.txt`.
  'seeded_beans_with_color_name.txt' - is the finalize data ready to be seeded into the API with all 'Bean' properties.
  'list_of_colors.txt' - a supporting file - table that list all the hex color code that exist in the seeded data, include the color nickname.
