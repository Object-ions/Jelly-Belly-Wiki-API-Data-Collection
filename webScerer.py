import requests
from bs4 import BeautifulSoup

def scrape_jelly_belly_flavor_details():
    # URL of the Jelly Belly Flavor Collections page
    url = 'https://www.jellybelly.com/jelly-belly-flavor-collections'

    # Setting a user-agent to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

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
                    group_name = div.find('h2').get_text(strip=True)
                    print(f"Group Name: {group_name}")

                    # Iterate over each flavor <li>
                    for li in div.find_all('li', {'aria-label': 'bean'}):
                        try:
                            # Extract background color
                            style = li.get('style')
                            background_color = style.split(';')[0].split(': ')[1] if style else 'No Background Color'
                            
                            # Extract image URL
                            image = li.find('img')
                            image_url = image['src'] if image else 'No Image URL'

                            # Extract flavor name
                            flavor_name = li.find('p', class_='blue-text').get_text(strip=True) if li.find('p', class_='blue-text') else 'No Flavor Name'

                            print(f"\tFlavor Name: {flavor_name}")
                            print(f"\tBackground Color: {background_color}")
                            print(f"\tImage URL: {image_url}\n")
                        except IndexError as e:
                            print("\tAn error occurred while processing a flavor item:", e)
            else:
                print("Flavor details section not found")
        else:
            print(f"Failed to retrieve the page. Status Code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
scrape_jelly_belly_flavor_details()
