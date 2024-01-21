import requests
from bs4 import BeautifulSoup
import os
import base64
from urllib.parse import urlparse, unquote


def valid_filename(url):
    """
    Create a valid filename from a URL by keeping only the last part after the last slash
    and removing any invalid characters.
    """
    parsed = urlparse(url)
    filename = os.path.basename(unquote(parsed.path))
    return filename.split('?')[0].split('&')[0]


# Downloader. Saves an image from a given URL.
def download_image(url, folder):
    try:
        if url.startswith('data:image'):
            # Handle Base64 encoded images
            header, encoded = url.split(",", 1)
            file_ext = header.split(";")[0].split("/")[1]
            file_name = f"image.{file_ext}"
            with open(os.path.join(folder, file_name), "wb") as file:
                file.write(base64.b64decode(encoded))
        else:
            # Handle normal image URLs
            response = requests.get(url)
            if response.status_code == 200:
                file_name = valid_filename(url)
                with open(os.path.join(folder, file_name), 'wb') as file:
                    file.write(response.content)
    except Exception as e:
        print(f"Error downloading {url}: {e}")


# A crawler to extract images from a given website
def crawl_images(webpage_url, folder='downloaded_images'):
    # Creates a folder if not created
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = requests.get(webpage_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    base_url = f"{response.url.split('/')[0]}//{response.url.split('/')[2]}"

    # For all the tags <img> extracts the URLs and passes them into the downloader.
    for img_tag in soup.find_all('img'):
        img_url = img_tag.get('src')
        if img_url:
            if not img_url.startswith('http'):
                img_url = base_url + img_url
            download_image(img_url, folder)


webpage_url = 'https://www.deviantart.com/tag/memes'  # Any URL of a website that contains images
crawl_images(webpage_url)
