from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import json

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set the path to chromedriver executable
webdriver_service = Service("/Users/imac/Downloads/chrome-mac-x64/chromedriver.app/Contents/MacOS/GoogleChromeforTesting")

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

url = "https://www.jellybelly.com/jelly-belly-single-flavors"

driver.get(url)

# Wait for the dynamically loaded elements to show up
time.sleep(5)

# Extracting information
elements = driver.find_elements(By.CLASS_NAME, "flavor-item")

data = []

for element in elements:
    # Extracting the details as per your requirement
    img_src = element.find_element(By.CLASS_NAME, "large-bean-image").get_attribute('src')
    title = element.find_element(By.CLASS_NAME, "title").text
    short_desc = element.find_element(By.CLASS_NAME, "shortDesc").text
    recipe = element.find_element(By.CLASS_NAME, "recipe").text
    read_more_link = element.find_element(By.CLASS_NAME, "readmoreAbout").get_attribute('href')
    ingredients = element.find_element(By.CLASS_NAME, "ingredients").text

    item = {
        "Image": img_src,
        "Title": title,
        "Description": short_desc,
        "Recipe": recipe,
        "Link": read_more_link,
        "Ingredients": ingredients
    }

    data.append(item)

driver.quit()

# Save the scraped data to a JSON file
with open("/Users/imac/Desktop/webScrape/scraped_data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
