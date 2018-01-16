from mailing import *
from weather import *
from birds import  *
import schedule
import time

def main():
    emails = get_emails()
    print(emails)

    plan = get_plan()
    print(plan)

    forecast_info = get_weather_forecast()
    print(forecast_info)

    observations = obs.get_observations()
    print(observations)

    must_have_info = obs.check_must_have()
    print(must_have_info)

    send_emails(emails, plan, forecast_info, observations, must_have_info)

main()

# schedule.every().friday.at('12:00').do(main)

# while True:
  #  schedule.run_pending()
   # time.sleep(.1)