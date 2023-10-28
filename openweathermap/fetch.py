import requests
import json


origin_url = "http://api.openweathermap.org/data/2.5/weather?q=Lenting,de&APPID=0d6c009b39a7ddbd4b2905e1815f8347"

response = requests.get(origin_url)

jsonResponse = json.loads(response.text)

print("Sicaklik: "+str(jsonResponse["main"]["temp"]- 273)+ " *C")
print("Basinc: "+str(jsonResponse["main"]["pressure"])+ " Paskal.")
print("Nem Orani: "+str(jsonResponse["main"]["humidity"])+ "%")
