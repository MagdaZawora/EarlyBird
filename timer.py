import datetime

def day_of_week():
    if datetime.date.today().strftime("%A") == 'Thursday':
        return 'yes!'
    else:
        return 'no'

print(day_of_week())