from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Initialize ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Optional: run without opening a browser window
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to the page
driver.get('https://www.jellybelly.com/jelly-belly-bean-recipes')

# Initialize WebDriverWait
wait = WebDriverWait(driver, 10)

try:
    # Wait for the element that contains the recipes to be visible
    recipes_element = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="mz-drop-zone-recipecontent"]/div/div/div/div/section/div[1]/div/div/div[6]')))

    # Find all the 'block-container80' elements within the recipes element
    recipe_blocks = recipes_element.find_elements(By.CLASS_NAME, 'block-container80')

    # Array to store the recipes
    recipes_array = []

    # Extract information from each recipe block
    for block in recipe_blocks:
        # Extract the recipe name
        recipe_name = block.find_element(By.CLASS_NAME, 'headline-beans').find_element(By.TAG_NAME, 'h2').text
        # Extract the 'alt' attributes from images, replacing 'plus' and 'equals'
        ingredient_images = block.find_elements(By.TAG_NAME, 'img')
        ingredients = [img.get_attribute('alt').replace('plus', '+').replace('equals', '=') for img in ingredient_images]

        # Add the recipe name as the final element in the ingredient list
        ingredients.append(recipe_name)
        
        # Add the ingredients list to the recipes array
        recipes_array.append(ingredients)

except TimeoutException:
    print('The page took too long to load or the element could not be found.')

# Close the browser
driver.quit()

# Output the result
print(recipes_array)
