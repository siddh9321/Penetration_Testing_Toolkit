import requests

def run(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url).json()
    
    print("\nLocation Info:")
    for key, value in response.items():
        print(f"{key}: {value}")
    
    return response