from mailing import *
from weather import *
from birds import  *

def main():
    emails = get_emails()
    print(emails)

    plan = get_plan()
    print(plan)

    forecast_info = get_weather_forecast()
    print(forecast_info)

    observations = get_observations()
    print(observations)

    send_emails(emails, plan, forecast_info, observations)

main()