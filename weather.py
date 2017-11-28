import requests


def get_weather_forecast():
    r = requests.get(
        'http://api.openweathermap.org/data/2.5/forecast?lat=41&lon=-76&units=metric&APPID={}')
    forecast = r.json()
    description = forecast['list'][0]['weather'][0]['description']
    # print(description)
    temp_min = forecast['list'][0]['main']['temp_min']
    temp_max = forecast['list'][0]['main']['temp_max']
    # print(temp_min, temp_max)
    pressure = forecast['list'][0]['main']['pressure']
    # print(pressure)
    if temp_min >= 0:
        forecast_info = 'Weather forecast for tomorrow is '
        forecast_info += description + ' with pressure of ' + str(pressure) + ' hPa, a high of ' + str(
            int(temp_max)) + ' degrees'
        forecast_info += ' and a low of ' + str(int(temp_min)) + ' degrees.'
    else:
        forecast_info = 'Weather forecast for tomorrow is '
        forecast_info += description + ' with pressure of ' + str(pressure) + ' hPa, a high of ' + str(
            int(temp_max)) + ' degrees'
        forecast_info += ' and a low of ' + str(int(temp_min)) + ' degrees.' + '\n'
        forecast_info += 'A bit freezing, so have sometning warming up with you:)'
    return forecast_info


# get_weather_forecast()
