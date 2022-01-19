from bs4 import BeautifulSoup
import requests
# run file in python console
# Web Scrapping - weather of USA
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=35.22073000000006&lon=-83.42010999999997#.Yeaeb_5BzIU')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-list') # shows weather updates of seven days from today
items = soup.find_all(class_='tombstone-container')

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]  # list comprehension
short_description = [item.find(class_='short-desc').get_text() for item in items]
temperature = [item.find(class_='temp').get_text() for item in items]

print(period_names)
print(short_description)
print(temperature)

#pandas -- Table Format
import pandas as pd

weather_stuff = pd.DataFrame(
    {
        'period': period_names,
        'short_description': short_description,
        'temperature': temperature,
    }
)

print(weather_stuff)
weather_stuff.to_csv('weather.csv') # getting weather details of seven days into csv file