import requests

def get_weather_forecast(url):
    r = requests.get(url)
    forecast = r.json()
    description = forecast['list'][0]['weather'][0]['description']
    print(description)
    temp_min = forecast['list'][0]['main']['temp_min']
    temp_max = forecast['list'][0]['main']['temp_max']
    print(temp_min, temp_max)
    pressure = forecast['list'][0]['main']['pressure']
    print(pressure)
    forecast_info = {'description': description, 'temp_min': temp_min, 'temp_max': temp_max, 'pressure': pressure}
    return forecast_info

#print(get_weather_forecast(
  # 'http://api.openweathermap.org/data/2.5/forecast?lat=41&lon=-76&units=metric&APPID='))
