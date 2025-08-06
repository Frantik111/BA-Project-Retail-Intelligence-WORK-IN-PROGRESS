@echo off
setlocal EnableDelayedExpansion

echo [1/3] Inštalujem Flask...
call "%~dp0winpython\python-3.12.3\python.exe" -m pip install flask

echo [2/3] Vytváram odkaz...
powershell -Command ^
"$shortcutPath = \"$env:APPDATA\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\BluetoothSniffer.lnk\"; ^
$shell = New-Object -ComObject WScript.Shell; ^
$shortcut = $shell.CreateShortcut($shortcutPath); ^
$shortcut.TargetPath = \"%~dp0winpython\\python-3.12.3\\pythonw.exe\"; ^
$shortcut.Arguments = \"%~dp0app\\skript.py\"; ^
$shortcut.WorkingDirectory = \"%~dp0app\"; ^
$shortcut.Save()"

echo [3/3] Hotovo. Bluetooth sniffer bude spustený po prihlásení.
pause
