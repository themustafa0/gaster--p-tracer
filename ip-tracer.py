import requests
import time 
from os import system
import os
os.system("title Gaster IP-Tracer")

print(r"""

   ____           _              ___ ____     _____                        
  / ___| __ _ ___| |_ ___ _ __  |_ _|  _ \   |_   _| __ __ _  ___ ___ _ __ 
 | |  _ / _` / __| __/ _ \ '__|  | || |_) |____| || '__/ _` |/ __/ _ \ '__|
 | |_| | (_| \__ \ ||  __/ |     | ||  __/_____| || | | (_| | (_|  __/ |   
  \____|\__,_|___/\__\___|_|    |___|_|        |_||_|  \__,_|\___\___|_|   
                                                                                                           
    """)

time.sleep(2)

# degiskenler ve printler
time.sleep(3)
system("cls||clear")
print("Hosgeldiniz")

ip_adress = input("IP Address Girin: ")
url = f'https://ipinfo.io/{ip_adress}/json'

response = requests.get(url)

# :)
data = response.json()
city = data['city']
region = data['region']
country = data['country']
loc = data['loc']

print(f"""
        IP Adresi: {ip_adress}
        Sehir: {city}
        Bolge: {region}
        Ulke: {country}
        Konum: {loc}
        Guncelleme Tarihi: {time.strftime('%d-%m-%Y %H:%M:%S')}
        """)
time.sleep(2)
print("IP Logger 15 Saniye içinde kapanacaktır.")
time.sleep(15)