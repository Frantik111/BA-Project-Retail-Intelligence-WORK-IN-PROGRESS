import subprocess
import re
import datetime
import time
import logging
import socket
import os

# Nastavenie logovania
logging.basicConfig(filename="wifi_scanner.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def scan_wifi_networks():
    try:
        result = subprocess.run(["netsh", "wlan", "show", "networks", "mode=bssid"],
                                capture_output=True, text=True)
        output = result.stdout

        networks = []
        current_ssid = None
        bssid = None

        for line in output.splitlines():
            ssid_match = re.match(r"^\s*SSID\s+\d+\s+:\s+(.*)", line)
            bssid_match = re.match(r"^\s*BSSID\s+\d+\s+:\s+(.*)", line)
            signal_match = re.match(r"^\s*Signal\s+:\s+(\d+)%", line)

            if ssid_match:
                current_ssid = ssid_match.group(1)
            elif bssid_match and current_ssid:
                bssid = bssid_match.group(1)
            elif signal_match and current_ssid and bssid:
                signal_strength = int(signal_match.group(1))
                networks.append({
                    "timestamp": datetime.datetime.now().isoformat(),
                    "ssid": current_ssid,
                    "bssid": bssid,
                    "signal_percent": signal_strength
                })

        return networks

    except Exception as e:
        logging.error(f"Chyba pri skenovaní sietí: {e}")
        return []

def get_interface_info():
    try:
        result = subprocess.run(["netsh", "wlan", "show", "interfaces"],
                                capture_output=True, text=True)
        output = result.stdout

        info = {}
        for line in output.splitlines():
            line = line.strip()
            if "MAC" in line and ":" in line:
                info["mac_address"] = line.split(":")[1].strip()
            elif "RSSI" in line and ":" in line:
                info["rssi_dbm"] = line.split(":")[1].strip()
            elif "SSID" in line and ":" in line and "BSSID" not in line:
                info["ssid"] = line.split(":")[1].strip()
            elif "BSSID" in line and ":" in line:
                info["bssid"] = line.split(":")[1].strip()
            elif "Signál" in line or "Signal" in line:
                info["signal_percent"] = line.split(":")[1].strip()

        return info

    except Exception as e:
        logging.error(f"Chyba pri získavaní informácií o rozhraní: {e}")
        return {}

    except Exception as e:
        logging.error(f"Chyba pri získavaní informácií o rozhraní: {e}")
        return {}


    except Exception as e:
        logging.error(f"Chyba pri získavaní informácií o rozhraní: {e}")
        return {}

def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        logging.error(f"Chyba pri získavaní IP adresy: {e}")
        return "Neznáma"

def main_loop(scan_interval=120):
    logging.info("Spúšťam Wi-Fi skener...")
    while True:
        networks = scan_wifi_networks()
        device_info = get_interface_info()
        ip_address = get_ip_address()

        logging.info(f"Zariadenie: MAC={device_info.get('mac_address')}, IP={ip_address}, RSSI={device_info.get('rssi_dbm')} dBm")

        for net in networks:
            logging.info(f"SSID={net['ssid']}, BSSID={net['bssid']}, Signal={net['signal_percent']}%")

        time.sleep(scan_interval)

if __name__ == "__main__":
    main_loop(scan_interval=20)  
