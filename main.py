import requests
import json
import msvcrt

print("_______  ___ ")
print("  /  _/ _ \/ _ \___ ___ ____ ")
print(" _/ // ___/ , _/ -_) _ `/ _ \ ")
print("/___/_/  /_/|_|\__/\_,_/ .__/")
print("                      /_/    ")
print("                             v1")

ip = input("IP Address: ")

response = requests.get(f'https://ipapi.co/{ip}/json')
info = response.json()
readable_info = json.dumps(info, indent=4)
print(readable_info)
msvcrt.getch()