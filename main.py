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

    special_info = check_special()
    print(special_info)

    send_emails(emails, plan, forecast_info, observations, special_info)

main()