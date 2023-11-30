import requests
from bs4 import BeautifulSoup

def scrape_jelly_belly_flavors():
    # URL of the page to scrape
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
            
            # Find the <ul> element with class 'flavors'
            flavors_list = soup.find('ul', class_='flavors')
            
            if flavors_list:
                # Iterate over each <li> element within the <ul>
                for li in flavors_list.find_all('li'):
                    # Extract and print the text from each <li>
                    print(li.text.strip())
            else:
                print("Flavor list not found")
        else:
            print(f"Failed to retrieve the page. Status Code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
scrape_jelly_belly_flavors()
