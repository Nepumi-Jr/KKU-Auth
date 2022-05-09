import requests
import configparser
from getpass import getpass
import time

SEC_CONST = 1.2
TEST_URL = "https://www.google.com"
AUTH_URL = "https://nac05.kku.ac.th/login"

def tryToPing(url:str):
    isNetConnected = True
    try:
        testConnection = requests.get(url)
    except:
        return False,"No Internet or error"
        
    if isNetConnected:
        if testConnection.status_code != 200:
            return False, f"Can't connect to Login ({testConnection.status_code})"
        else:
            return True, "Yatta"



secWaitNow = 1
#? Make sure that you are connect to KKU Wifi
while True:
    print("Try to Connect to login KKU...", end = "")

    isConnect, msg = tryToPing(AUTH_URL)
    if isConnect:
        print("Connected to KKU Yey!")
        break
    else:
        print(msg)

    print("Please make sure you're connect to KKU Wifi")
    print(f"Retring in {secWaitNow:.1f}s...")
    secWaitNow *= SEC_CONST
    time.sleep(secWaitNow)

while True:

    payload = {
        'username': input("Give me ya usr name : "),
        'password': getpass("Give me ya password : "),
    }

    headers = {'User-Agent': 'Mozilla/5.0'}

    result =  requests.post(AUTH_URL, payload, headers=headers)
    print(f"Try to ping {TEST_URL}...", end = "")
    isConnect, msg = tryToPing(TEST_URL)
    if isConnect:
        print("Connected to INTERNET!!!")
        break
    else:
        print(msg)
    print("Please re-login...\n")


