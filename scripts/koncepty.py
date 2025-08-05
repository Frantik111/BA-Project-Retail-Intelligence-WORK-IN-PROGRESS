import subprocess
result = subprocess.run(["powershell", "-Command", "Get-Service"], capture_output=True, text=True)
print(result.stdout)


import subprocess

cmd = ["powershell", "-Command", "Get-Service | Where-Object {$_.Status -eq 'Running'}"]
result = subprocess.run(cmd, capture_output=True, text=True)
print(result.stdout)

#2. Bezpečne pracuj s parametrami
#Nepoužívaj reťazce s vloženými premennými bez kontroly.
#Používaj zoznam argumentov (list) v subprocess.run().

service_name = "wuauserv"
cmd = ["powershell", "-Command", f"Get-Service -Name '{service_name}'"]

# 3. Zachytávaj chyby a výstup
# Vždy kontroluj returncode a stderr.
result = subprocess.run(cmd, capture_output=True, text=True)
if result.returncode != 0:
    print("Chyba:", result.stderr)
else:
    print("Výstup:", result.stdout)

# 4. Vyhýbaj sa dočasným súborom
# Nepíš PowerShell skripty do .ps1 súborov, ak to nie je nutné.

# Vkladaj skript priamo do -Command.


#ak máš dlhý kód s variabilnými hodnotami, ktorý chceš odoslať do powershellu
user = "Zdenko"
ps_code = f"""
$User = '{user}'
Write-Output "Hello, $User!"
"""
cmd = ["powershell", "-Command", ps_code]
result = subprocess.run(cmd, capture_output=True, text=True) 
print(result.stdout)

# Obojsmerná komunikácia: Python ↔ PowerShell
# Môžeš posielať vstup do PowerShellu cez stdin:
ps_code = "param($name) Write-Output \"Hello, $name!\""
cmd = ["powershell", "-Command", ps_code]
result = subprocess.run(cmd, input="Zdenko", capture_output=True, text=True)
print(result.stdout)

# 10. Spracovanie výstupu ako JSON
# Ak chceš výstup z PowerShellu spracovať v Pythone, používaj ConvertTo-Json:

cmd = ["powershell", "-Command", "Get-Process | Select-Object -First 5 | ConvertTo-Json"]
result = subprocess.run(cmd, capture_output=True, text=True)
import json
processes = json.loads(result.stdout)
print(processes[0]["ProcessName"])

#Príklad: Získanie zoznamu súborov
folder = "C:\\Users\\Zdenko\\Documents"
cmd = ["powershell", "-Command", f"Get-ChildItem -Path '{folder}' | Select-Object Name"]
result = subprocess.run(cmd, capture_output=True, text=True)
print(result.stdout)


# bluethooth vytiahne základné informácie
import subprocess

def scan_bluetooth():
    cmd = [
        "powershell",
        "-Command",
        "Get-PnpDevice -Class Bluetooth | Select-Object Status, Class, FriendlyName, InstanceId"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

print(scan_bluetooth())

# bluetooth získa kompletné informácie
import subprocess

def scan_bluetooth_detailed():
    cmd = [
        "powershell",
        "-Command",
        "Get-PnpDevice -Class Bluetooth | Format-List *"
    ]
    #tu je alternatíva na vyskúšanie
    #Get-CimInstance Win32_PnPEntity | Where-Object { $_.Name -like "*Bluetooth*" } | Format-List *
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

print(scan_bluetooth_detailed())


import subprocess

def scan_wifi():
    cmd = ["netsh", "wlan", "show", "networks", "mode=bssid"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

print(scan_wifi())