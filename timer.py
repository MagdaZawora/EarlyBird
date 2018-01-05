import datetime
import schedule
import time
import smtplib


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


def send_emails(emails, plan):
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.starttls()
    email_from = input('Enter email address: ')
    password = input('Enter password: ')
    server.login(email_from, password)
    for name, email_to in emails.items():
        message = 'Subject: Time to do some bird-watching!\n'
        message += 'Hi ' + name + '!\n\n'
        message += plan + '\n\n'
        message += 'Hope to see you tomorrow!'
        server.sendmail(email_from, email_to, message)
    server.quit()


def job():

    # if datetime.date.today().strftime("%A") == 'Friday':

        emails = get_emails()
        print(emails)

        plan = get_plan()
        print(plan)

        send_emails(emails, plan)

schedule.every(10).seconds.do(job)
schedule.every().friday.at("15:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
