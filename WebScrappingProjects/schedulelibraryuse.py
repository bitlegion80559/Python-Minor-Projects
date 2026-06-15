import os
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time
import schedule
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
            writer=csv.writer(f)
            writer.writerow(["timestamp","coin","price"])
        
    with open(filename,'a',newline='',encoding='utf-8') as f:
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer=csv.writer(f)
        for coin in data:
            writer.writerow([timestamp,coin['id'],coin['current_price']])


def job():
    data=get_data()
    save_data_CSV(data)

schedule.every().hour.at(":00").do(job)
while True:
    schedule.run_pending()
    time.sleep(60)






