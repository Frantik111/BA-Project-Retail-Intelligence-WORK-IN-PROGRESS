# import subprocess

# result = subprocess.run(
#     ["wmic", "printer", "get", "name,status"],
#     capture_output=True,
#     text=True
# )
# print(result.stdout)


# import subprocess

# result = subprocess.run(
#     ["powershell", "-Command", "Get-PrintJob"],
#     capture_output=True,
#     text=True
# )
# print(result.stdout)

import subprocess

command = 'powershell "Get-CimInstance -ClassName Win32_StartupCommand | Select-Object Name, Command, Location"'
result = subprocess.run(command, capture_output=True, text=True, shell=True)
print(result.stdout)
