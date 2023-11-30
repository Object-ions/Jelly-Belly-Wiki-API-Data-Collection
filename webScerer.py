import requests
from bs4 import BeautifulSoup
import json

def scrape_jelly_belly_flavor_details_to_json():
    # URL of the Jelly Belly Flavor Collections page
    url = 'https://www.jellybelly.com/jelly-belly-flavor-collections'

    # Setting a user-agent to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Data structure to hold all flavors
    all_flavor_data = []

    try:
        # Send GET request with a timeout and custom headers
        response = requests.get(url, headers=headers, timeout=10)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all <div> elements with class 'flavor-coll-details'
            flavor_details = soup.find_all('div', class_='flavor-coll-details')

            if flavor_details:
                for div in flavor_details:
                    # Extract the flavor group name
                    group_name = div.find('h2').get_text(strip=True) if div.find('h2') else 'No Group Name'

                    # Iterate over each flavor <li>
                    for li in div.find_all('li', {'aria-label': 'bean'}):
                        flavor_info = {}
                        try:
                            # Extract background color
                            style = li.get('style')
                            background_color = style.split(':')[1].strip(';').strip() if style else 'No Background Color'
                            
                            # Extract image URL
                            image = li.find('img')
                            image_url = image['src'] if image else 'No Image URL'

                            # Extract flavor name
                            flavor_name = li.find('p').get_text(strip=True) if li.find('p') else 'No Flavor Name'

                            # Add flavor info to the list
                            flavor_info = {
                                'Group Name': group_name,
                                'Flavor Name': flavor_name,
                                'Background Color': background_color,
                                'Image URL': image_url
                            }
                            all_flavor_data.append(flavor_info)

                        except IndexError as e:
                            print("\tAn error occurred while processing a flavor item:", e)
            else:
                print("Flavor details section not found")

            # Write data to JSON file
            with open('jelly_belly_flavors.json', 'w', encoding='utf-8') as json_file:
                json.dump(all_flavor_data, json_file, indent=4, ensure_ascii=False)

        else:
            print(f"Failed to retrieve the page. Status Code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
scrape_jelly_belly_flavor_details_to_json()
