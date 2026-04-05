# Penetration Testing Toolkit 🛡️

**Python-based modular penetration testing toolkit** with multiple features for learning, demo, and portfolio purposes.  
This toolkit is designed for **educational & demo purposes only**.

---

## Features

- **Port Scanner**: Scan target IPs for open ports.
- **Brute Force**: Test login credentials using wordlists.
- **Banner Grabber**: Fetch server banners to identify technologies.
- **GeoIP Lookup**: Find location, ISP, and other info of IPs.
- **Vulnerability Scanner**: Detect demo vulnerabilities (SQL Injection, XSS, Directory Traversal).
- **HTML Report Generation**: Generates a professional report in `reports/report.html`.

---

## Demo Output

Example report snippet:
Port Scanner: Open Ports - 80, 443, 22
Brute Force: Success! Username: admin | Password: admin123
Banner Grabber: Apache/2.4.7 (Ubuntu)
GeoIP: Ashburn, Virginia, United States
Vulnerabilities:
[+] SQL Injection
[+] XSS
[+] Directory Traversal


---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<username>/Penetration_Testing_Toolkit.git
cd Penetration_Testing_Toolkit

pip install -r requirements.txt
python main.py

Penetration_Testing_Toolkit/
│   main.py
│   requirements.txt
│
├───modules/
│   ├── port_scanner.py
│   ├── brute_forcer.py
│   ├── banner_grabber.py
│   ├── geoip_lookup.py
│   └── vuln_scanner.py
│
├───utils/
│   └── report_generator.py
│
├───reports/
│   └── report.html
│
└───wordlists/
    └── passwords.txt
