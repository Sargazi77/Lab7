from pprint import pprint
import os
import requests
from datetime import datetime

#http://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us,&units=imperial&appid=2fe5bdfa54f7cee8984d19c59dce6c0d 
key = os.environ.get('WEATHER_KEY')
querry = {'q': 'minneapolis,us','units': 'imperial', 'appid': key}

url ='http://api.openweathermap.org/data/2.5/forecast'

data = requests.get(url, params=querry).json()

#pprint(data) 
list_of_forcast = data['list']

for forcast in list_of_forcast:
    temp = forcast['main']['temp']
    timestamp = forcast['dt']
    forcast_date = datetime.fromtimestamp(timestamp)
    wind_speed = forcast['wind']['speed']



    #print(temp, forcast_date)
    print(f'At {forcast_date} the tempreture will be {temp} degreees F and the wind speed is {wind_speed} MPH')



