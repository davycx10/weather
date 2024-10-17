import requests

city_name = input("mettre le nom de la ville souhaité: ")

langage = "fr" # la sortie de la langue est en français
key = "288dadf7b5d8930928ac12107a4682e8"
api_link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}&lang={langage}"

# Récupérer les données JSON
response = requests.get(api_link)
data = response.json()

if 'weather' in data and len(data['weather']) > 0:
    description = data['weather'][0]['description']
    print("Description :", description)
    temp_kelvin = data['main']['temp']
    temp_celsius = temp_kelvin - 273.15  # Conversion de Kelvin à Celsius
    print("Température :", round(temp_celsius, 2),"°C")  # Affiche la température
    humidity = data['main']['humidity'] #affiche l'humidité 
    print("Humidity :", humidity)
else:
    print("Aucune donnée météo disponible.")

# Affiche la réponse complète si besoin
#print(data)

