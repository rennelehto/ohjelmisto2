import json
import requests

hakusana = input("Syötä kaupungin nimi: ")
pyyntö = f'https://api.openweathermap.org/data/2.5/weather?q={hakusana}&appid=26cd9d15b940db1dbe4b89c329c122df&units=metric&lang=fi'

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        #print(json.dumps(json_vastaus, indent=2))
        sää =json_vastaus["weather"][0]["description"]
        lämpö= json_vastaus["main"]["temp"]

        print(f'Kaupungin {hakusana.capitalize()} sää: {sää}, lämpötila: {lämpö}°C.')


except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")