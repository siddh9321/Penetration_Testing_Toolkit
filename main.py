from modules import port_scanner, brute_forcer, banner_grabber, geoip_lookup, vuln_scanner
from utils.report_generator import generate_report

def menu():
    print("""
1. Port Scanner
2. Brute Force
3. Banner Grabber
4. GeoIP Lookup
5. Vulnerability Scanner
6. Exit
""")

data = []

while True:
    menu()
    choice = input("Select option: ")

    # 🔎 PORT SCANNER
    if choice == "1":
        target = input("Enter IP: ")
        result = port_scanner.run(target)

        if result:   # <-- safety
            data.extend([f"Open Port: {p}" for p in result])

    # 🔑 BRUTE FORCE
    elif choice == "2":
        url = input("Enter login URL: ")
        username = input("Username: ")

        result = brute_forcer.run(url, username, "wordlists/passwords.txt")

        if result:
            data.append(f"Brute Force Success: {result}")
        else:
            data.append("Brute Force Failed")

    # 🌐 BANNER GRABBER
    elif choice == "3":
        target = input("Enter IP: ")
        result = banner_grabber.run(target)

        if result:
            data.append(f"Banner: {result}")

    # 🌍 GEOIP LOOKUP
    elif choice == "4":
        ip = input("Enter IP: ")
        result = geoip_lookup.run(ip)

        if result:
            data.append(f"GeoIP: {result}")

    # 🛡️ VULNERABILITY SCANNER
    elif choice == "5":
        url = input("Enter URL: ")
        result = vuln_scanner.run(url)

        if result:   # <-- important fix
            data.extend(result)
        else:
            data.append("No vulnerabilities found / Connection failed")

    # ❌ EXIT + REPORT
    elif choice == "6":
        generate_report(data)
        print("✅ Report Generated! Check reports/report.html")
        break

    # ⚠️ INVALID INPUT
    else:
        print("❌ Invalid option! Please try again.")