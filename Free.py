'''import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.3387&lon=-121.8854')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-list')

items = week.find_all(class_='tombstone-container')

period_names = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temps = [item.find(class_='temp').get_text() for item in items]

weather = pd.DataFrame(
    {'period': period_names,
     'short_descriptions': short_desc,
     'temperatures': temps
     })

print(weather)
'''
print('hello world you are dumb')