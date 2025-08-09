import sqlite3
from sqlite3 import Error
from datetime import datetime, timezone
import json
import asyncio
from flask import Flask, jsonify
import threading
import bluetooth
from bleak import BleakScanner
from collections import deque
import signal, sys


fronta_udajov = deque()
zamok_fronty = threading.Lock()

def pridaj_do_fronty(data):
    with zamok_fronty:
        fronta_udajov.append(data)

### Operácie spojené s databázou
database_path="logs.db"
default_table="""CREATE TABLE IF NOT EXISTS devices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                name TEXT,
                address TEXT,
                rssi INTEGER,
                manufacturer_data TEXT,
                service_uuids TEXT,
                tx_power INTEGER,
                device_type TEXT,
                device_details TEXT,
                service_data TEXT,
                local_name TEXT
                )
                """

def batch_store_to_db():
    global fronta_udajov
    with zamok_fronty:
        if not fronta_udajov:
            return
        else:
            zaznamy = list(fronta_udajov)
            fronta_udajov.clear()
            conn = create_connection(database_path)
            if conn is not None:
                cursor = conn.cursor()
                try:
                    conn.executemany(
                                        """INSERT INTO devices (
                                        timestamp, name, address, rssi, manufacturer_data, service_uuids, 
                                        tx_power, device_type, device_details, service_data, local_name
                                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                                        """
                                        ,zaznamy)
                    conn.commit()
                    print("Úspešne sa vykonal dotaz")
                except Error as e:
                    print("Nastala chyba:", e)
                finally:
                    conn.close()
            else:
                print("Spojenie s databázou sa nepodarilo")

def create_connection(database_path):
    """Use of database, basic function for connection"""
    conn = None #if except, no conn created also extra error
    try:
        conn = sqlite3.connect(database_path, check_same_thread=False, timeout=30) #check_same_thread=False aby nebol problém u async
        conn.execute("PRAGMA journal_mode=WAL;")
        print("Úspešne som sa pripojil na databázu")
    except Error as e:
        print("Nastala chyba:", e)
    return conn

### nie je určené pre neustálu prácu, iba pre občasne zápisy, ideálne odstrániť
def execute_query(query, parms = None):
    conn = create_connection(database_path)
    if conn is not None:
        cursor = conn.cursor()
        try:
            if parms:
                cursor.execute(query, parms)
            else:
                cursor.execute(query)
            conn.commit()
            print("Úspešne sa vykonal dotaz")
        except Error as e:
            print("Nastala chyba:", e)
        finally:
            conn.close()
    else:
        print("Spojenie s databázou sa nepodarilo")
    
def init_db():
    """For first start of the application"""
    execute_query(default_table)
    
### pôvodná funkcia, ktorá nie je vhodná
# def save_device_data(name, address, rssi, manufacturer_data, service_uuids, tx_power, device_type, device_details, service_data, local_name):
#     timestamp = datetime.now(timezone.utc).isoformat()
#     query =f"""INSERT INTO devices (
#                         timestamp, name, address, rssi, manufacturer_data, service_uuids, 
#                         tx_power, device_type, device_details, service_data, local_name
#                         ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#             """
#     params = (
#             timestamp,
#             name,
#             address,
#             rssi,
#             str(manufacturer_data),
#             str(service_uuids),
#             tx_power,
#             str(device_type),
#             str(device_details),
#             service_data,
#             local_name    
#     )
#     execute_query(query, params)

def get_data(query):
    conn = create_connection(database_path)
    result = None
    if conn is not None:
            cursor = conn.cursor()
            try:
                cursor.execute(query)
                result = cursor.fetchall()
                print("Úspešne sa načítali údaje")
                return result
            except Error as e:
                print("Nastala chyba:", e)
            finally:
                conn.close()
    else:
        print("Spojenie s databázou sa nepodarilo")
    
                
### Operácie spojené s Bluetooth
def scan_classic():
    try:
        discovered_devices = bluetooth.discover_devices(duration=8, flush_cache=True, lookup_names=True, lookup_class=True)
        for address, name, device_type in discovered_devices:
            timestamp = datetime.now(timezone.utc).isoformat()
            pridaj_do_fronty((timestamp, name, address, None, None, None, None, str(device_type), None, None, None))
    
    except bluetooth.BluetoothError as e:
        print("Nastala chyba Classic:", e)
            
    
async def scan_ble():
    try:
        discovered_devices = await BleakScanner.discover(timeout = 8, return_adv = True)
        for address, (device, adv_data) in discovered_devices.items():
            try:
                device_details_serialized = json.dumps(device.details)
            except TypeError:
                device_details_serialized = str(device.details)
            timestamp = datetime.now(timezone.utc).isoformat()
            pridaj_do_fronty((
                timestamp,                 
                device.name or "Neznáme", 
                address, 
                device.rssi, 
                str(adv_data.manufacturer_data),
                str(adv_data.service_uuids),
                adv_data.tx_power,
                "BLE", 
                str(device_details_serialized),
                str(adv_data.service_data),
                adv_data.local_name
                ))
    except Exception  as e:
        print("Nastala chyba BLE:", e)
        
### Operácie spojené s Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Bluetooth scanner is running. Visit /history for logs."

@app.route("/history")
def get_history():
    rows = get_data("SELECT * FROM devices ORDER BY id DESC LIMIT 10") or []
    columns = [
        "id", "timestamp", "name", "address", "rssi", "manufacturer_data",
        "service_uuids", "tx_power", "device_type", "device_details",
        "service_data", "local_name"
    ]
    # Prevedie každý riadok na dict: {stĺpec: hodnota}
    return jsonify([dict(zip(columns, row)) for row in rows])

### Inicializácia celého skriptu
def start_flask():
    app.run(port=5000)

async def main_loop(interval_seconds = 10):
    while True:
        print(f"\n Nový cyklus: {datetime.now(timezone.utc).isoformat()}")
        scan_classic()
        await scan_ble()
        await asyncio.sleep(interval_seconds)
        
async def save_loop(interval_seconds = 60):
    while True:
        print(f"\n Ukladám do databázy: {datetime.now(timezone.utc).isoformat()}")
        batch_store_to_db()
        await asyncio.sleep(interval_seconds)        

async def runner():
    await asyncio.gather(main_loop(), save_loop())

def start_asyncio():
    asyncio.run(runner())
    

def safe_exit(signum, frame):
    print("Ukončujem aplikáciu")
    batch_store_to_db()
    sys.exit(0)

if __name__ == "__main__":
    init_db()
    signal.signal(signal.SIGINT, safe_exit)
    flask_thread = threading.Thread(target=start_flask)
    runner_thread = threading.Thread(target=start_asyncio)

    flask_thread.start()
    runner_thread.start()
    
    flask_thread.join()
    runner_thread.join()

