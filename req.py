import requests
import sys
from time import sleep


R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'
HEADER = '\033[95m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'

def get(num, delay):
    url = "https://gimmeproxy.com/api/getProxy?minSpeed=500"
    for x in range(num):
        req = requests.get(url)
        try:
            proxy = req.json()['ipPort']
            print(G + proxy)
        except KeyError:
            print(R + "[!] ip banned: waiting....")
            sleep(delay)

    print(G + "\n[>] " + C + "done")


if __name__ == '__main__':
    if len(sys.argv) == 3:
        try:
            fl = int(sys.argv[1])
            delay = int(sys.argv[2])
        except:
            print(R+"\n[!] error: use number")
            sys.exit()
        print(C + f"\n[+] requesting {fl} proxies.........\n")
        get(fl, delay)
    else:
    	print("Usage: python req.py [number of proxies] [delay] \n\nExample:\n\tpython main.py 10 3")
