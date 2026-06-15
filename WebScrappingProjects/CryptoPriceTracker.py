import os
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import matplotlib.pyplot as plt
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

def graph_plotting(coin_name):
    times=[]
    prices=[]
    with open(filename,'r',encoding='utf-8')as f:
        reader=csv.DictReader(f)
        for row in reader:
            if row['coin']==coin_name:
                times.append(row['timestamp'])
                prices.append(float(row['price']))
    if not times:
        print(f"No data found for {coin_id}")
        return
    
    plt.figure(figsize=(10,5))
    plt.plot(times, prices, marker='o')
    plt.tight_layout()
    plt.grid()
    plt.show()

def main():
    data=get_data()
    save_data_CSV(data)
    coin_name=input("Enter the coin name to plot the graph: ")
    if coin_name:
        graph_plotting(coin_name)

if __name__=="__main__":    
    main()





