import requests
from bs4 import BeautifulSoup
import json

# URL of the website to scrape
url = 'https://www.jellybelly.com/jelly-belly-bean-recipes'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the parent element with class "recipe-container"
recipe_container = soup.find('div', class_='recipe-container')

# Initialize a list to store the extracted information
output_list = []

# Find all the child div elements with class "block-container80" inside the parent element
child_containers = recipe_container.find_all('div', class_='block-container80')

# Iterate through the child containers and extract the desired information
for i, container in enumerate(child_containers):
    # Extract the text from the h2 element inside the div with class "headline-beans"
    h2_text = container.find('div', class_='headline-beans').h2.text.strip()

    # Extract the "alt" attribute from all img elements within the <ul> tag
    img_alt_list = [img['alt'] if img.get('alt') else img['src'].split('/')[-1].split('.')[0].replace("icon-", "").replace("R", "+") for img in container.ul.find_all('img')]

    # Add the h2_text as the first element of the list
    img_alt_list.insert(0, h2_text)

    # Append the extracted list to the output list
    output_list.append(img_alt_list)

# Create a dictionary with the extracted information
output_dict = {i: output_list[i] for i in range(len(output_list))}

# Save the dictionary as a JSON file
with open('recipe.json', 'w', encoding='utf-8') as json_file:
    json.dump(output_dict, json_file, ensure_ascii=False, indent=4)

print("Data saved to 'recipe.json'.")
