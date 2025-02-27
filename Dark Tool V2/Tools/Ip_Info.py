import os
import requests

ip = input("Enter IP: ")
response = requests.get(f"http://ip-api.com/json/{ip}")
data = response.json()

if data["status"] == "fail":
    print("Invalid IP address!")
else:
    print("\nIP Information:")
    print(f"IP: {data['query']}")
    print(f"Country: {data['country']}")
    print(f"Region: {data['regionName']}")
    print(f"City: {data['city']}")
    print(f"ISP: {data['isp']}")
    print(f"AS: {data['as']}")
    print(f"Lat: {data['lat']}, Lon: {data['lon']}")

input("\nPress Enter to return to menu...")  

os.system('cls' if os.name == 'nt' else 'clear')  
