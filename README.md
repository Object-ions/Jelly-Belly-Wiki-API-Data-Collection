# Jelly Belly API Data Collection and Processing Workflow

## Overview
This document outlines the workflow used for scraping, processing, and preparing Jelly Belly flavor data for API integration.

### 1. Data Collection

#### Static Data Scraping (`staticScraper.py`)
- **Purpose**: Scrapes static data from the Jelly Belly flavor collections webpage.
- **Data Collected**:
  - Group Name
  - Flavor Name
  - Background Color
  - Image URL
- **Output**: Data exported to `jelly_belly_flavors.json`.

#### Dynamic Data Scraping (`dynamicScraper.py` & `getXpathsBtns.py`)
- **getXpathsBtns.py**:
  - Identifies and extracts XPath of buttons on the Jelly Belly single flavors webpage that trigger data fetching.
  - **Output**: XPaths saved in `button_xpaths.json`.
- **dynamicScraper.py**:
  - Uses these XPaths to control ChromeDriver to click on buttons and scrape dynamic data (Flavor Name, Description, Ingredients).
  - **Output**: Data exported to `dynamic_data.json`.

### 2. Data Merging and Cleaning

#### Merging Data (`mergeBeansData.py`)
- Normalizes and merges data from `static_data.json` and `dynamic_data.json`. Remove duplicates and adding a sequential BeanId to each entry.
- Tracks and exports unmatched items from both datasets.
- **Outputs**:
  - Merged data in `merged_beans_data.json`.
  - Unmatched static data in `unmatched_static_data.json`.
  - Unmatched dynamic data in `unmatched_dynamic_data.json`.

### 3. Data Validation

#### Searching for Missing Names (`searchForMissingNames.py`)
- Compares expected flavor list (`beans_name_list.json`) with actual entries in `merged_beans.json`.
- Identifies and displays missing flavors.

### 4. Data Formatting

#### Capitalization (`toCapitalize.py`)
- Capitalizes strings in the data, excluding specific keys.
- **Output**: Processed data in `main_results_capitalized.json`.

#### Preparation for API Seeding (`prepToSeed.py`)
- Formats data for seeding into the API.
- **Note**: Specific operations of this script are not detailed yet.