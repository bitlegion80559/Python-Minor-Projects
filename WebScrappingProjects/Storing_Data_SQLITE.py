import requests
from datetime import datetime
import sqlite3
import time

BASE_URL= "https://api.coingecko.com/api/v3/coins/markets"
DB_NAME="crypto_data.db"
PARAMS={
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page':10,
    'page':1,
    'sparkline':False
}

def fetch_data():
    response=requests.get(BASE_URL,params=PARAMS)
    return response.json()
def create_table():
    conn=sqlite3.connect(DB_NAME)
    cur=conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS crypto_prices(
                id Integer PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                coin TEXT,
                price REAL
                )
''')
    conn.commit()
    conn.close()

def store_database(data):
    conn=sqlite3.connect(DB_NAME)
    cur=conn.cursor()
    timestamp=datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    for coin in data:
        cur.execute('''
            INSERT INTO crypto_prices(timestamp,coin,price) VALUES(?,?,?)
                    ''', (timestamp,coin['id'],coin['current_price']))
    conn.commit()
    conn.close()

def search_coin(coin_name):
    conn=sqlite3.connect(DB_NAME)
    cur=conn.cursor()
    cur.execute('''
        SELECT timestamp,price FROM crypto_prices Where coin=?
                ORDER BY timestamp DESC LIMIT 1
    ''',(coin_name,))
    result=cur.fetchone()
    conn.close()
    if result:
        print(f"${result[1]} - {result[0]}")

def main():
    create_table()
    print("1. Fetch and store crypto data")
    print("2. Search latest price for a coin")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        data = fetch_data()
        store_database(data)
    elif choice == "2":
        coin_name = input("Enter coin name: ").strip().lower()
        search_coin(coin_name)
    else:
        print("Invalid option")
main()



