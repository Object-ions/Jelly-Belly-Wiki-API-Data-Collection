import requests
from bs4 import BeautifulSoup

def scrape_jelly_belly_flavor_collections():
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
                # Iterate over each <div> element
                for div in flavor_details:
                    # Extract and print the text from each <div>
                    print(div.text.strip())
            else:
                print("Flavor collection details not found")
        else:
            print(f"Failed to retrieve the page. Status Code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
scrape_jelly_belly_flavor_collections()
