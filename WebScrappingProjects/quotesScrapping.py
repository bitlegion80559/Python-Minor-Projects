import os
import requests
from bs4 import BeautifulSoup
import textwrap
from urllib.parse import urljoin
from PIL import Image , ImageDraw , ImageFont

BASE_URL="https://quotes.toscrape.com/"
OUTPUT_DIR="quotes"

def get_data():
    try:
        response=requests.get(BASE_URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {BASE_URL}: {e}")
        return []
    
    soup=BeautifulSoup(response.text,'html.parser')
    quotes=[]
    div_content=soup.select('div.quote')
    # print(div_content)
    for div in div_content:
        text=div.select_one('span.text').get_text().strip("“”")
        author=div.select_one('small.author').get_text().strip()
        quotes.append((text,author))

    return quotes

def create_image(quote,author,index):
    width,height=800,400
    background_color=(255,255,198)
    text_color=(0,0,0)
    image=Image.new('RGB',(width,height),background_color)
    draw=ImageDraw.Draw(image)
    font=ImageFont.load_default()
    wrapped_text=textwrap.fill(quote,width=60)
    y_text=60
    draw.text((50,y_text),wrapped_text,fill=text_color,font=font)
    y_text+=wrapped_text.count('\n')*2+40
    draw.text((400,y_text),f"- {author}",fill=text_color,font=font)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    filename=os.path.join(OUTPUT_DIR,f"quote_{index+1}.png")
    image.save(filename)


def main():
    quotes=get_data()

    for index,(quote,author)in enumerate(quotes):
        create_image(quote,author,index)


if __name__=="__main__":
    main()

