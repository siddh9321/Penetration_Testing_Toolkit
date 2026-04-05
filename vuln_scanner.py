import requests

def run(url):
    payloads = ["' OR 1=1--", "<script>alert(1)</script>"]
    results = []   # <-- important

    for payload in payloads:
        test_url = url + payload
        try:
            r = requests.get(test_url, timeout=5)

            if payload in r.text:
                print(f"[!] Vulnerable to: {payload}")
                results.append(f"Vulnerable: {test_url}")
            else:
                print(f"[-] Not vulnerable: {payload}")

        except requests.exceptions.RequestException as e:
            print(f"[!] Could not connect: {e}")
            results.append(f"Error: {test_url}")

    return results   # <-- MUST return list