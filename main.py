from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
import os

# Initialize Chrome Options
chrome_options = webdriver.ChromeOptions()

# Set up Chrome Driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the website and interact with it
driver.get("https://www.jellybelly.com/jelly-belly-single-flavors")
button = driver.find_element(By.XPATH, """//*[@id="a-w-cream-soda"]/button""")
button.click()

# Find elements and extract their text
description_elements = driver.find_elements(By.XPATH, """//*[@id="descriptionContainer"]""")
extracted_data = []

# Check if the file exists and load existing data
if os.path.exists("main_results.json"):
    with open("main_results.json", "r") as file:
        extracted_data = json.load(file)

# Extract and append new data
for element in description_elements:
    text_parts = element.text.split('\n')
    
    # Extract relevant parts based on their position
    flavor_name = text_parts[1]
    description = text_parts[2]
    ingredients = text_parts[6]

    # Append to list as dictionary
    extracted_data.append({
        "FlavorName": flavor_name,
        "Description": description,
        "Ingredients": ingredients
    })

# Write the results to a JSON file
with open("main_results.json", "w") as file:
    json.dump(extracted_data, file, indent=4)

# Close the driver
driver.quit()

print("Results saved to main_results.json")
