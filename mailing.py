import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from weather import get_weather_forecast
from birds import get_observations, check_must_have

def get_emails():
    emails = {}
    try:
        emails_file = open('emails.txt', 'r')
        for line in emails_file:
            (name, email_to) = line.split(',')
            emails[name] = email_to.strip()
        emails_file.close()
    except FileNotFoundError as err:
        print(err)
    return emails


def get_plan():
    try:
        plan_file = open('plan.txt', 'r')
        plan = plan_file.read().strip()
        plan_file.close()
    except FileNotFoundError as err:
        print(err)
    return plan


def send_emails(emails, plan, forecast_info, observations, must_have_lst):

        MESSAGE_TEMPLATE = '''  
        Subject: {0}\n\n
        Hi {1}!\n
        Some interesting sighting have been recently noticed:\n
        {2}.\n        
        Weather forecast for tomorrow is {3} with pressure of {4} hPa, a high of {5} degrees and a low of {6} degrees.\n         
        Plan for tomorrow:\n        
        {7}\n
        Hope to see you tomorrow!
        '''
        SUBJECT = 'Time to do some bird-watching!'

        server = smtplib.SMTP('smtp.gmail.com', '587')
        server.starttls()
        email_from = input('Enter email address: ')
        password = input('Enter password: ')
        server.login(email_from, password)

        for name, email_to in emails.items():
            msg = MESSAGE_TEMPLATE.format(SUBJECT, name, ', '.join(observations), forecast_info['description'],
                                              forecast_info['pressure'], forecast_info['temp_max'],
                                              forecast_info['temp_min'], plan)
            server.sendmail(email_from, email_to, msg)
        server.quit()




