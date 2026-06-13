import requests
from bs4 import BeautifulSoup
import csv

URL="https://news.ycombinator.com/"
FILE= "HackerNews.csv"
def get_headings():
    try:
        response=requests.get(URL,timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
        return []
    
    soup=BeautifulSoup(response.text,'html.parser')
    data=soup.select("span.titleline > a")
    # print(data)
    arr=[]
    for link in data:
        text=link.get_text(strip=True)
        links=link.get('href')
        arr.append({
            "text":text,
            "link":links
        })
    print("Scrappeed data successfully.")
    return arr

def import_to_CSV(data):
    if not data:
        print("No data to write to CSV.")
        return
    
    with open (FILE,'w',newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=["text","link"])
        writer.writeheader()
        writer.writerows(data)

    print("Data has been Successfully written to CSV file.")


def main():
    get_data=get_headings()
    import_to_CSV(get_data)


if __name__=="__main__":
    main()

