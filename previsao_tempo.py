import requests
import os
import time
time.sleep(1)
os.system('clear')
time.sleep(1)

print("""
========================================
                 Autor:
========================================
""")
os.system('figlet Willian')
print("""
========================================
             Clima da cidade""")
time.sleep(4)

#Minha API abaixo:
API_KEY = "c53804142281f803c220debe120c7643"

cidade = input('Digite a cidade: ')
print('Clima na cidade de:', cidade)

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}"

requests = requests.get(link)
requests_dic = requests.json()
descricao = requests_dic["weather"][0]["description"]
temperatura = requests_dic["main"]["temp"] -273.15
print(descricao, temperatura)

print("""

  OBRIGADO POR UTILIZAR ESTE PROGRAMA!
""")
time.sleep(2)
