# This script will generate the xpath for the target elements

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

# Navigate to the website
driver.get("https://www.jellybelly.com/jelly-belly-single-flavors")

# Find all 'Learn More' buttons by their aria-controls attribute
buttons = driver.find_elements(By.CSS_SELECTOR, "li.single button[aria-controls='flavor-content']")

# List to hold all the xpaths
button_xpaths = []

for button in buttons:
    # Find the parent 'li' element
    parent_li = button.find_element(By.XPATH, '..')
    parent_id = parent_li.get_attribute("id")
    if parent_id:
        xpath = f"//li[@id='{parent_id}']/button[@aria-controls='flavor-content']"
        button_xpaths.append(xpath)

# Close the driver
driver.quit()

# Save the xpaths to a JSON file
with open("get_xpaths_btn.json", "w") as file:
    json.dump(button_xpaths, file, indent=4)

print("XPaths saved to get_xpaths_btn.json")
