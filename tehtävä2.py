import requests
import json

Kysely = input("Ilmoita paikkakunta: ")

pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={Kysely},fi&appid=df2f23555b8bb70eff10e105302daa5f&units=metric&lang=fi"

vastaus = requests.get(pyynto).json()

print(vastaus["weather"][0]["description"])
print(f'{vastaus["main"]["temp"]} c')
