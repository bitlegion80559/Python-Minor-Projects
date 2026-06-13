import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/States_and_union_territories_of_India"
def get_headings():
    try:
        headers ={
            "User-Agent": "Mozilla/5.0"
        }
        response=requests.get(URL,timeout=10, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Unexpected error occured while fetching the page: {e} ")
    
    soup=BeautifulSoup(response.text,'html.parser')
    # print(soup)
    h2_tags=soup.find_all('h2')
    arr=[]
    # print(h2_tags)
    for h2 in h2_tags:
        text=h2.get_text()
        arr.append(text)
    return arr

print(get_headings())

