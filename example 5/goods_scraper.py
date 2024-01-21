import requests
from bs4 import BeautifulSoup


def fetch_item_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('div', class_=lambda x: x and 'search-item-card-wrapper-gallery' in x)
    for item in items:
        title = item.find('div', {'title': True}).get('title')

        # Parsing the price (considering partial class name match)
        price_container = item.find('div', class_=lambda x: x and 'multi--price-sale-' in x)
        if price_container:
            price_parts = price_container.find_all('span')
            price = ''.join(span.text for span in price_parts)
        else:
            price = "Price not found"

        amount_sold = item.find('span', class_=lambda x: x and 'multi--trade--' in x)
        amount_sold_text = amount_sold.text if amount_sold else "Amount sold not found"

        print(f"Title: {title}, Price: {price}, Amount Sold: {amount_sold_text}", flush=True)


# Fetches items based on the keyword provided
keyword = "Latvia"
search_url = f'https://www.aliexpress.com/w/wholesale-{keyword}.html'  # Replace with the actual search URL
fetch_item_details(search_url)
