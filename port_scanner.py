import socket
from concurrent.futures import ThreadPoolExecutor
from config import MAX_THREADS
from utils.logger import log

open_ports = []

def scan_port(target, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        open_ports.append(port)
        log(f"Port {port} open")
        print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        pass

def run(target):
    print(f"\nScanning {target}...\n")
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        for port in range(1, 1000):
            executor.submit(scan_port, target, port)
    return open_ports