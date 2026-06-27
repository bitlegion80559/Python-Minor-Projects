import os
import psutil
import time

def clear_Screen():
    os.system('cls' if os.name=='nt' else 'clear')

def show_stats():
    cpu=psutil.cpu_percent(interval=1)
    ram=psutil.virtual_memory()
    disk=psutil.disk_usage('/')

    print(f"{cpu} {ram} {disk}")

if __name__=="__main__":
    try:
        while True:
            clear_Screen()
            show_stats()
            time.sleep(3)
    except KeyboardInterrupt:
        print("Monitoring Stopped.....")