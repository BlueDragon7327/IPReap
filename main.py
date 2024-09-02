import requests
import json
import msvcrt
ip = input("IP Address: ")

response = requests.get(f'https://ipapi.co/{ip}/json')
info = response.json()
readable_info = json.dumps(info, indent=4)
print(readable_info)
msvcrt.getch()