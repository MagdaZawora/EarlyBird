from mailing import get_emails, get_plan, send_emails
from weather import get_weather_forecast
from birds import  get_observations, check_must_have
import schedule
import time

def main():

    emails = get_emails()
    print(emails)

    plan = get_plan()
    print(plan)

    forecast_info = get_weather_forecast(
        'http://api.openweathermap.org/data/2.5/forecast?lat=41&lon=-76&units=metric&APPID=')
    print(forecast_info)

    observations = get_observations(
        'http://ebird.org/ws1.1/data/obs/hotspot/recent?r=L99381&back=5&maxResults=500&detail=simple&locale=en_US&fmt=xml')
    # print(observations)

    must_have_info = check_must_have(get_observations(
    'http://ebird.org/ws1.1/data/obs/hotspot/recent?r=L99381&back=5&maxResults=500&detail=simple&locale=en_US&fmt=xml'),
        ['Canada Goose', 'Bald Eagle'])
    print(must_have_info)

    send_emails(emails, plan, forecast_info, observations, must_have_info)

main()

# schedule.every().friday.at('12:00').do(main)

# while True:
  #  schedule.run_pending()
   # time.sleep(.1)