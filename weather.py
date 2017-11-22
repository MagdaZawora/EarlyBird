import requests

def get_weather_forecast():
    r = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=Krakow,pl&units=metric&APPID=')
    forecast = r.json()
    description = forecast['list'][0]['weather'][0]['description']
    print(description)
    temp_min = forecast['list'][0]['main']['temp_min']
    temp_max = forecast['list'][0]['main']['temp_max']
    print(temp_min, temp_max)
    pressure = forecast['list'][0]['main']['pressure']
    print(pressure)

    text_mail = 'Weather forecast for tomorrow is '
    text_mail += description + ' with pressure of ' + str(pressure) + ' hPa, a high of ' + str(int(temp_max)) + ' degrees'
    text_mail += ' and a low of ' + str(int(temp_min)) + ' degrees.'
    return print(text_mail)

get_weather_forecast()