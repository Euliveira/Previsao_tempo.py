import requests

#Minha API abaixo:
API_KEY = "c53804142281f803c220debe120c7643"

cidade = 'São Paulo'
print('Agora na cidade de São Paulo :')

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}"

requests = requests.get(link)
requests_dic = requests.json()
descricao = requests_dic["weather"][0]["description"]
temperatura = requests_dic["main"]["temp"] -273.15
print(descricao, temperatura)

print("""

                 OBRIGADO!
""")
time.sleep(2)
