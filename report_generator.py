def generate_report(data):
    with open("reports/report.html", "w") as f:
        f.write("<html><body><h1>Scan Report</h1><ul>")
        for item in data:
            f.write(f"<li>{item}</li>")
        f.write("</ul></body></html>")