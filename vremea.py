import requests
import json
API_KEY="83e6257a1f5c3f33b11b1f6c28ae89ac"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"
city=input("Introdu numele orasului: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
rasp = requests.get(requests_url)
data = json.loads(rasp.text)
print(data)
if rasp.status_code == 200:
    data = rasp.json()
    vremea =data['weather'][0]['description']
    temp = round(data["main"]["temp"] -273.15, 2)
    vitezaVant = data['wind']["speed"]
    unghi = data['wind']["deg"]
    print("Vremea: ", vremea)
    print("Temperatura: ", temp, " C")
    print("Viteza vantului: ",vitezaVant, " si unghiul ", unghi)
else:
    print("Avem o eroare :| ")