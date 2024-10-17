import requests

#demander les donner de l'API
response = requests.get('https://public-api.meteofrance.fr/public/arpege/1.0', params={'stations': 'PARIS'}) 

#Parser les donnée JSON
data = response
