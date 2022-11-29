from bs4 import BeautifulSoup
from requests import get

URL = 'https://pogoda.interia.pl/'

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')

def parse_city(city):
    return str(city.replace(',', ''))

for weather in bs.find_all('section', class_ = 'weather-places-group cities-weather is-legend'): #pobieramy html tabeli
    city = weather.find('ul', class_ = 'weather-index').get_text().split()

    #print(*city, sep = '\n')

    break
data = []
for x in range(0,len(city),2):
   data.append([{city[x]: city[x+1]}])
   if x == 28:
       break

text = ''
city = iter(city[:-3])
for x in city:
    text += x +": " + next(city) + "\n"
print(text)

