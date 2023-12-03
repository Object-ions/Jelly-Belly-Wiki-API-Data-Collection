from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os

# Initialize Chrome Options
chrome_options = webdriver.ChromeOptions()

# Set up Chrome Driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the website
driver.get("https://www.jellybelly.com/jelly-belly-single-flavors")

# Load the XPaths from the file
with open("button_xpaths.json", "r") as file:
    button_xpaths = json.load(file)

# Initialize the data list
extracted_data = []

# Check if the results file already exists
if os.path.exists("main_results.json"):
    with open("main_results.json", "r") as file:
        extracted_data = json.load(file)

# Loop through each XPath and extract data
for xpath in button_xpaths:
    try:
        # Wait until the button is clickable
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        button.click()

        # Wait for the description container to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, """//*[@id="descriptionContainer"]"""))
        )

        # Extract the data
        description_element = driver.find_element(By.XPATH, """//*[@id="descriptionContainer"]""")
        text_parts = description_element.text.split('\n')
        flavor_name = text_parts[1] if len(text_parts) > 1 else ""
        description = text_parts[2] if len(text_parts) > 2 else ""
        ingredients = text_parts[6] if len(text_parts) > 6 else ""

        extracted_data.append({
            "FlavorName": flavor_name,
            "Description": description,
            "Ingredients": ingredients
        })

    except Exception as e:
        print(f"An error occurred while processing {xpath}: {e}")

# Write the results to a JSON file
with open("main_results.json", "w") as file:
    json.dump(extracted_data, file, indent=4)

# Close the driver
driver.quit()

print("Results saved to main_results.json")
