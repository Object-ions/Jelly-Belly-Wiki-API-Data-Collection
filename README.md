# Jelly Belly Wiki API Data Collection (and Processing)

### By Moses Atia Poston

## [Project Description](#project-description)

This repository contains scripts and supporting files for data collection. It is part of a larger project divided into three segments (list below). It focuses on the data collection and processing data for the Jelly Belly API, primarily using Python for web scraping from the official Jelly Belly website. The objective is to automate the scraping, processing, and preparation of Jelly Belly bean data for API integration.

This project is divided into three main segments, each with its own repository:

1. [Jelly Belly Wiki API Data Collection](#)(this repo): This repository contains scripts and supporting files for data collection using Python, BeautifulSoup, and ChromeDriver. It details the methodology used for creatively gathering data step by step until it was ready to be seeded into the C# API.
2. [Jelly Belly Wiki API](https://github.com/Object-ions/Jelly-Belly-Wiki-API): The heart of the project, this repository holds the C# and EF Core .Net API with MySql migrations. It serves as the core database of the project. Detailed instructions on how to use this API are available in the repository, similar to the API Documentation provided in the UI.
3. [Jelly Belly Wiki Client](https://github.com/Object-ions/Jelly_Belly_Wiki_Client): The User Interface makes full use of the API's database, showcasing one approach to design by utilizing all the endpoints and their various options.

## [Live versions](#live)

[Jelly Belly Wiki - UI](https://jelly-belly-wiki.netlify.app/)
[Jelly Belly Wiki - API](https://jellybellywikiapi.onrender.com/)

- The UI deployed on Netlify.com
- The API deployed on Render.com
- The database deployed on TiDB.com

## Table of Contents

1. [Project Description](#project-description)
2. [Live version of the UI](#live)
3. [Technologies Used](#technologies-used)
4. [Setup / How to Use the Scripts](#setup--how-to-use-the-scripts)
5. [Scraping and Data Processing](#scraping-and-processing)
   - A. ['Bean' class scraping process](#bean-scraping)
   - B. ['Recipe' class scraping process](#recipe-scraping)
   - C. ['Fact' class scraping process](#fact-scraping)
6. [Copyright and Data Accuracy Disclaimer](#copyright-and-data-accuracy-disclaimer)
   - A. [Content Origin](#content-origin)
   - B. [Disclaimer](#disclaimer)
   - C. [Consumer Advice](#consumer-advice)
7. [Known Bugs](#known-bugs)
8. [License](#license)
9. [contact](#contact)

## [Technologies Used](#technologies-used)

- Python (for web scraping and data processing)
- Selenium WebDriver (for dynamic data scraping)
- BeautifulSoup (for static data scraping)
- JSON (for data storage and processing)
- Artificial Intelligence (AI - ChatGPT 4): Utilized for retrieving 'facts' and formatting the output.

## [Setup / How to Use the Scripts](#setup--how-to-use-the-scripts)

To use the scripts in this repository, follow these step-by-step instructions:

1. **Install Python**:

   - First, check if Python is already installed on your system. Open your command line interface (CLI / Terminal) and type the following command to check your Python version:
     ```
     python --version
     ```
   - If Python is not installed, or if you have an older version, you can install the latest version of Python by downloading it from the official website. However, for macOS and Linux systems, Python can be installed directly from the terminal using package managers.

     - **For macOS**, use Homebrew by typing:
       ```
       brew install python
       ```
     - **For Linux** (Debian-based systems like Ubuntu), use APT by typing:
       ```
       sudo apt-get update
       sudo apt-get install python3
       ```

   - During installation, make sure to select the option 'Add Python to PATH' to ensure Python is accessible from the command line.

2. **Install Required Python Packages**:

   - Open your command line interface (CLI), such as Command Prompt (Windows) or Terminal (macOS/Linux).
   - Install the necessary Python packages by running the following commands:
     - `pip install selenium`: Installs Selenium WebDriver for browser automation.
     - `pip install bs4`: Installs BeautifulSoup for parsing HTML and extracting data.
     - `pip install webdriver_manager`: Installs WebDriver Manager, a tool to manage browser drivers easily.

3. **Running the Scripts**:
   - Download or clone this repository to your local machine.
   - Navigate to the repository's directory using the command line.
   - Run the scripts in the order specified under "Bean Class Scraping Process" and "Recipe Class Scraping Process":
     - Use the command `python <script_name>.py` to run a script. For example, to run the `staticScraper.py` script, type `python staticScraper.py`.
   - Follow the on-screen instructions or prompts (if any) while the scripts are running.

By following these steps, you can set up your environment and run the scripts to collect and process data from the Jelly Belly website. Remember to run the scripts in the order they are listed in the "Bean Class Scraping Process" and "Recipe Class Scraping Process" sections for optimal results and to avoid errors.

## [Scraping and Data Processing](#scraping-and-processing)

### ['Bean' class scraping process](#bean-scraping)

### 1. Data Collection

#### Static Data Scraping (`staticScraper.py`)

- **Purpose**: This script is designed to scrape static data from the Jelly Belly flavor collections webpage. It specifically collects details about different Jelly Belly flavors, including their group names, individual flavor names, background colors, and associated image URLs.
- **Input**: The script uses the URL 'https://www.jellybelly.com/jelly-belly-flavor-collections' to scrape data.
- **Output**: Data exported to `static_data.json`.

#### Dynamic Data Scraping (`dynamicScraper.py` & `getXpathsBtns.py`)

- **Purpose**:

  - `getXpathsBtns.py`: This script is designed to generate XPath expressions for target elements, specifically 'Learn More' buttons, on the Jelly Belly single flavors webpage. It uses these XPath expressions to facilitate the dynamic scraping of flavor data.

    - **Input**: The script navigates to 'https://www.jellybelly.com/jelly-belly-single-flavors' to find the target elements.
    - **Output**: `get_xpaths_btn.json` - Contains the XPath expressions for the buttons on the webpage.

  - `dynamicScraper.py`: This script scrapes dynamic data from the Jelly Belly single flavors webpage using the XPaths generated by `getXpathsBtns.py`. It collects details such as flavor name, description, and ingredients.
    - **Input**: The script uses the XPaths from `get_xpaths_btn.json` to click on buttons and scrape dynamic content from the same Jelly Belly webpage.
    - **Output**: dynamic_data.json - The scraped dynamic data, including flavor name, description, and ingredients, is saved in this JSON file.

### 2. Data Merging and Cleaning

#### Merging Data (`mergeBeansData.py`)

- **Purpose**:
  - This script is designed to load, normalize, and merge data from `static_data.json` and `dynamic_data.json`. It ensures the data is consistent by normalizing the FlavorName field and merges the datasets based on this field. The script also keeps track of and exports any unmatched items from both datasets.
- **Process**:
  - **Normalization**: Flavor names from both datasets are normalized for consistency.
  - **Merging**: Merges the normalized data based on the FlavorName field.
  - **Tracking Unmatched Data**: Identifies and separates items that do not find a match in either dataset.
  - **Additional Fields**: Adds default values for fields like 'GlutenFree', 'SugarFree', 'Seasonal', and 'Kosher' in the merged data.
- **Input**:
  - `static_data.json` and `dynamic_data.json` - The datasets to be merged.
- **Outputs**:
  - `merged_beans_data.json` - Contains the merged data with additional fields.
  - `unmatched_static_data.json` - Contains static data items that didn't find a match.
  - `unmatched_dynamic_data.json` - Contains dynamic data items that didn't find a match.

### 3. Data Validation

#### Searching for Missing Names (`searchForMissingNames.py`)

note : `beans_name_list.json` - is a copy of `get_xpaths_btn.json` with text modification - isolate bean's name from it's xpath.

- **Purpose**: Compares expected flavor list (`beans_name_list.json`) with actual entries in `merged_beans_data.json` (to make sure no information was omitted).
- Identifies and displays missing flavors in terminal.
- **Input**: `beans_name_list.json` and `merged_beans_data.json`.
- **Outputs**: list of 'missing' data identified by flavorName to the terminal.

### 4. Data Formatting

#### Capitalization (`toCapitalize.py`)

- **Purpose**: Capitalizes strings in the data, keys to capitalize = "GroupName", "FlavorName", "Description", "Ingredients".
- **Input**: Processed data in `merged_beans_data.json` (after checking no beans are missing).
- **Output**: `toCapitalize.json`.

#### Preparation for API Seeding (`prepDataToSeedWithColor.py`)

- **Purpose**:
  - Formats data for seeding into the API.
  - Add color information to each bean - the script finds the closest CSS3 color name to a given hex color `backgroundColor`
- **Input**: `toCapitalize.json`.
- **Output**: `seeded_beans_with_color_name.txt`, `list_of_colors.txt`.
  'seeded_beans_with_color_name.txt' - is the finalize data ready to be seeded into the API with all 'Bean' properties.
  'list_of_colors.txt' - a supporting file - table that list all the hex color code that exist in the seeded data, include the color nickname.

## ['Recipe' class scraping process](#recipe-scraping)

### 1. Data Collection

#### (`getRecipe.py`)

- **Purpose**: The purpose of this script is to automate the web scraping of a specific webpage (https://www.jellybelly.com/jelly-belly-bean-recipes), extract information about jelly bean recipes, and store the extracted data in a structured format.
- **Input**: The input for this script is the URL of the webpage (https://www.jellybelly.com/jelly-belly-bean-recipes) containing jelly bean recipes.
- **Outputs**: The main output of this script is a list (scrapedRecipe.txt) that contains information about jelly bean recipes, including their names and ingredients, and this list is printed to the console as the final output.

### 2. Data Formatting

#### (`scrapedRecipeFormat.txt`)

- **Purpose**: Modify the scraped data format (manually with VS Code keyboard shortcuts) to match an array of strings in preparation for seeding.
- **Input**: `scrapedRecipe.txt`
- **Outputs**: `scrapedRecipeFormat.txt`

#### (`prepRecipeToSeed.txt`)

- **Purpose**: Modify the array of strings data format to match the Recipe model in preparation for seeding.
- **Input**: `scrapedRecipeFormat.txt`
- **Outputs**: `RecipeReadyToSeed.txt`

## ['Fact' class scraping process](#fact-scraping)

### 1. Data Collection and formatting

#### (`factsReadyToSeed.txt`)

- **Purpose**: Retrieve 100 facts about Jelly Belly beans using an AI prompt, and subsequently, prompt the AI to format the data to prepare it for feeding into the 'Fact' model.
- **Input**: Prompt: Generate 100 interesting and informative facts about Jelly Belly beans. Once you have the facts, please format the data in a way that it can be readily used for training the 'Fact' model (the prompt includes set of rules for formatting)
- **Outputs**: `factsReadyToSeed.txt`

## [Known Bugs](#known-bugs)

- No known bugs.

## [Copyright and Data Accuracy Disclaimer](#copyright-and-data-accuracy-disclaimer)

### [Content Origin](#content-origin)

Please be aware that all data and information presented in this application, including the UI and the database, are derived from the official Jelly Belly website. This project does not claim originality of the content and acknowledges that all information is borrowed from publicly available sources.

### [Disclaimer](#disclaimer)

While every effort has been made to ensure the accuracy of the information, there may be instances of errors, typos, or inaccuracies. Therefore, this resource should not be solely relied upon, especially for health-related decisions. I do not assume responsibility for the content's accuracy.

### [Consumer Advice](#consumer-advice)

Before consuming any Jelly Belly products, it is strongly advised to consult the official Jelly Belly website or product packaging to verify ingredients, calorie content, and other nutritional information. This step is crucial for those with dietary restrictions or allergies.

## [License](#license)

[MIT](https://choosealicense.com/licenses/mit/)

Copyright (c) 2023 Moshe Atia Poston.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### [contact](#contact)

If you detect any bug in the program, please reach out to me at [moshikoatia@gmail.com](mailto:moshikoatia@gmail.com).
