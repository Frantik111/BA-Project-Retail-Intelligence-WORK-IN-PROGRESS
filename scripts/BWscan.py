
from flask import Flask, jsonify
import sqlite3
import subprocess
import threading
import time

app = Flask(__name__)

# Funkcia, ktorá beží v pozadí
def background_scanner():
    global latest_output
    while True:
        resultblue = subprocess.run(
            ["powershell", "-Command", "Get-PnpDevice -Class Bluetooth | Format-List *"],
            #alternatívny kód Get-CimInstance Win32_PnPEntity | Where-Object { $_.Name -like "*Bluetooth*" } | Format-List *
            capture_output=True,
            text=True
        )
        resultwifi = subprocess.run(
            ["netsh", "wlan", "show", "networks", "mode=bssid"],
            capture_output=True,
            text=True
        )
        
        if resultblue.returncode == 0:
            output = resultblue.stdout.strip()
            if output:
                save_to_db(output)
            else:
                save_to_db("No Bluetooth devices found.")
        else:
            save_to_db(f"Error B: {resultblue.stderr}")
        
        if resultwifi.returncode == 0:
            output = resultwifi.stdout.strip()
            if output:
                save_to_db(output)
            else:
                save_to_db("No WIFI devices found.")
        else:
            save_to_db(f"Error W: {resultwifi.stderr}")
        time.sleep(5)  # každých 5 sekúnd


# Spustenie vlákna pri štarte aplikácie
threading.Thread(target=background_scanner, daemon=True).start()

# Endpoint na získanie aktuálneho výstupu

@app.route("/")
def index():
    return "Bluetooth scanner is running. Visit /history for logs."

@app.route("/history")
def get_history():
    conn = sqlite3.connect("logs.db")
    c = conn.cursor()
    c.execute("SELECT timestamp, output FROM logs ORDER BY id DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    return jsonify([{"timestamp": r[0], "output": r[1]} for r in rows])    
    
def init_db():
    conn = sqlite3.connect("logs.db", check_same_thread=False)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            output TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_to_db(output):
    conn = sqlite3.connect("logs.db", check_same_thread=False)
    c = conn.cursor()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO logs (timestamp, output) VALUES (?, ?)", (timestamp, output))
    conn.commit()
    conn.close()


# po spustení
init_db()


if __name__ == "__main__":
    app.run(port=5000)