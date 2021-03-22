import requests

respons = requests.get('https://www.ceneo.pl/63313139#tab=reviews')

print(respons.text)