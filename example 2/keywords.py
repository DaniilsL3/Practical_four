import requests
from urllib.parse import quote_plus

"""
This example is faulty, as it returns the redirection page (bot protection).
"""


# Define the search query
query = "RTU"


# Construct the search URL
url = f"https://www.google.com/search?q={query}"

# Send the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Process the response
    print(response.text)  # This will print the raw HTML of the search results page
else:
    print("Failed to retrieve search results")
    print(response.status_code)
