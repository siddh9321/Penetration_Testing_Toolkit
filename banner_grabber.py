import socket

def run(target):
    s = socket.socket()
    s.connect((target, 80))
    s.send(b"HEAD / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
    banner = s.recv(1024)
    print("\nBanner:\n", banner.decode())
    return banner.decode()