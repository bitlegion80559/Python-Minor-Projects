import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import wget

BASE_URL = "https://books.toscrape.com/"
IMAGE_DIR = "images"

def sanitize_filename(title):
    return re.sub(r'[^\w\-_. ]', '', title).replace(" ", "_")

def scrapping_and_download_images():
    try:
        response = requests.get(BASE_URL,timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {BASE_URL}: {e}")
        return
    soup=BeautifulSoup(response.text,"html.parser")

    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    books=soup.select("article.product_pod")[:10]

    for book in books:
        title=book.h3.a['title']
        relative_img=book.find("img").get("src")
        print(f"url - {relative_img}")
        img_url=urljoin(BASE_URL,relative_img)
        print(f"img_url - {img_url}")
        filename=sanitize_filename(title)+".jpg"
        filepath=os.path.join(IMAGE_DIR,filename)
        print(f"filepath - {filepath}")
        wget.download(img_url,filepath)
    


if __name__ == "__main__":
    scrapping_and_download_images()
