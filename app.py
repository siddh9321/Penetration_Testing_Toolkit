import tkinter as tk
from modules.port_scanner import run as port_scan

def start_scan():
    target = entry.get()
    result = port_scan(target)
    output.insert(tk.END, str(result) + "\n")

app = tk.Tk()
app.title("Penetration Toolkit")

entry = tk.Entry(app, width=30)
entry.pack()

btn = tk.Button(app, text="Scan Ports", command=start_scan)
btn.pack()

output = tk.Text(app)
output.pack()

app.mainloop()