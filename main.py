from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome Options
chrome_options = webdriver.ChromeOptions()

# Set up Chrome Driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Your existing code
driver.get("https://www.jellybelly.com/jelly-belly-single-flavors")
button = driver.find_element_by_xpath("""//*[@id="7up"]/button""")
button.click()

# Find elements in the opened container
description_elements = driver.find_elements_by_xpath("""//*[@id="descriptionContainer"]""")
for element in description_elements:
    print(element.text)

# Close the driver
driver.quit()