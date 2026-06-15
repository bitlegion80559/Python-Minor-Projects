import os
import requests
from bs4 import BeautifulSoup

URL="https://api.coingecko.com/api/v3/coins/markets"

PARAMS={
    'vs_currency':'usd',
    'order':'market_cap_desc',
    'per_page':20,
    'page':1,
    'sparkline':False
}
filename="crypto_data.csv"
def get_data():
    response=requests.get(URL, params=PARAMS)
    # print(response.json())
    return response.json()

def save_data_CSV(data):
    if not os.path.exists(filename):
        with open(filename,'w',newline='',encoding='utf-8') as f:
            f.write("timestamp","coin","price")

