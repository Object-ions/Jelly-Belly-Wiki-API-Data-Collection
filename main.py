from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json

# Initialize Chrome Options
chrome_options = webdriver.ChromeOptions()

# Set up Chrome Driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the website and interact with it
driver.get("https://www.jellybelly.com/jelly-belly-single-flavors")
button = driver.find_element(By.XPATH, """//*[@id="7up"]/button""")
button.click()

# Find elements and extract their text
description_elements = driver.find_elements(By.XPATH, """//*[@id="descriptionContainer"]""")
extracted_data = []

for element in description_elements:
    text_parts = element.text.split('\n')
    
    # Extract relevant parts based on their position
    flavor_name = text_parts[1]  # 2nd result
    description = text_parts[2]  # 3rd result
    ingredients = text_parts[6]  # 7th result

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
