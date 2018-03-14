import smtplib
from weather import *
from birds import *

def get_emails():
    emails = {}
    try:
        emails_file = open('emails.txt', 'r')
        for line in emails_file:
            (name, email_to) = line.split(',')
            emails[name] = email_to.strip()
    except FileNotFoundError as err:
        print(err)
    return emails


def get_plan():
    try:
        plan_file = open('plan.txt', 'r')
        plan = plan_file.read()
    except FileNotFoundError as err:
        print(err)
    return plan


def send_emails(emails, plan, forecast_info, observations, must_have_lst):
        server = smtplib.SMTP('smtp.gmail.com', '587')
        server.starttls()
        email_from = input('Enter email address: ')
        password = input('Enter password: ')
        server.login(email_from, password)
        for name, email_to in emails.items():
            message = 'Subject: Time to do some bird-watching!\n'
            message += 'Hi ' + name + '!\n\n'
            message += 'Some interesting sighting have been recently noticed: '
            message += observations + '\n'
            if must_have_lst:
                message += 'Please notice that among them ' + str(
                len(must_have_lst)) + ' from our "must-have" list: ' + ','.join(must_have_lst) + '!' + '\n\n'
            else:
                message += 'This time none from our "must-have" list, but still worth watching!'
            if forecast_info['temp_max'] >= 0:
                message += 'Weather forecast for tomorrow is '
                message += forecast_info['description'] + ' with pressure of ' + str(forecast_info['pressure']) + \
                           ' hPa, a high of ' + str(int(forecast_info['temp_max'])) + ' degrees'
                message += ' and a low of ' + str(int(forecast_info['temp_min'])) + ' degrees.'
            else:
                message += 'Weather forecast for tomorrow is '
                message += forecast_info['description'] + ' with pressure of ' + str(forecast_info['pressure']) + \
                           ' hPa, a high of ' + str(int(forecast_info['temp_max'])) + ' degrees'
                message += ' and a low of ' + str(int(forecast_info['temp_min'])) + ' degrees.' + '\n'
                message += 'A bit freezing, so have something warming up with you:)'
            message += plan + '\n\n'
            message += 'Hope to see you tomorrow!'
            server.sendmail(email_from, email_to, message)
        server.quit()


