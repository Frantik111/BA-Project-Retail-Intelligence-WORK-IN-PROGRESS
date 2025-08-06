
from flask import Flask, jsonify
from bleak import BleakScanner
from bleak.backends.winrt import WinRTBLEDevice

import asyncio
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
            text=True,
    	    creationflags=subprocess.CREATE_NO_WINDOW
        )
        resultwifi = subprocess.run(
            ["netsh", "wlan", "show", "networks", "mode=bssid"],
            capture_output=True,
            text=True,
	    creationflags=subprocess.CREATE_NO_WINDOW
        )
        
        if resultblue.returncode == 0:
            output = resultblue.stdout.strip()
            if output:
                save_to_db(output, "blue")
            else:
                save_to_db("No Bluetooth devices found.", "blue")
        else:
            save_to_db(f"Error B: {resultblue.stderr}", "blue")
        
        if resultwifi.returncode == 0:
            output = resultwifi.stdout.strip()
            if output:
                save_to_db(output, "wifi")
            else:
                save_to_db("No WIFI devices found.", "wifi")
        else:
            save_to_db(f"Error W: {resultwifi.stderr}", "wifi")
        time.sleep(5)  # každých 5 sekúnd


# Spustenie vlákna pri štarte aplikácie
# threading.Thread(target=background_scanner, daemon=True).start()

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
    c.execute("""
        CREATE TABLE IF NOT EXISTS logswifi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            output TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_to_db(output, table):
    conn = sqlite3.connect("logs.db", check_same_thread=False)
    c = conn.cursor()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    if table == "blue":
        c.execute("INSERT INTO logs (timestamp, output) VALUES (?, ?)", (timestamp, output))
    if table == "wifi":
        c.execute("INSERT INTO logswifi (timestamp, output) VALUES (?, ?)", (timestamp, output))
    conn.commit()
    conn.close()


def scan_ble():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    devices = loop.run_until_complete(BleakScanner.discover())

    if devices:
        for d in devices:
            try:
                info = (
                    f"Name: {d.name}, "
                    f"MAC: {d.address}, "
                    f"RSSI: {d.rssi}"
                )

                # Ak bežíš na Windows a ide o WinRTBLEDevice
                if isinstance(d, WinRTBLEDevice):
                    advertisement = d.details.advertisement
                    manufacturer_data = advertisement.manufacturer_data
                    local_name = advertisement.local_name

                    info += (
                        f", LocalName: {local_name}, "
                        f"ManufacturerData: {manufacturer_data}"
                    )
                else:
                    # fallback ak by to náhodou nebolo WinRT
                    info += f", RawDetails: {str(d.details)}"

            except Exception as e:
                info = f"Details error: {e}"

            save_to_db(info, "blue")
    else:
        save_to_db("No BLE devices found.", "blue")


def background_ble_scanner():
    while True:
        try:
            scan_ble()
        except Exception as e:
            save_to_db(f"BLE scan error: {str(e)}", "blue")
        time.sleep(5)

# uprava pre pynsist 
def main():
    init_db()
    threading.Thread(target=background_ble_scanner, daemon=True).start()
    app.run(port=5000)


if __name__ == "__main__":
    main()
    
    

#distribucia pynsist

