

import requests

# Specify the URL of the website you want to open
url = "https://sports.bet9ja.com/sport/soccer/1"

# Create a session and mount the HTTPS protocol with an HTTPAdapter configured for HTTP/1.1
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=3, pool_block=False)
session.mount("https://", adapter)

# Make a GET request to the URL with HTTP/1.1
response = session.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the content of the website
    print(response.text)
else:
    print("Failed to fetch the website. Status code:", response.status_code)
