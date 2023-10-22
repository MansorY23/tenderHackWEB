from email.utils import formataddr
from email.message import EmailMessage
import smtplib, ssl, csv

from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from crm import settings

from celery import shared_task
from typing import Union


def send_email():
    # first way
    msg = EmailMessage()
    msg['From'] = formataddr(('Ахтарьянов Арсений', 'arsa2003@mail.ru'))
    msg['To'] = formataddr(('Ахтарьянов Арсений', 'arsa2003@mail.ru'))
    msg['CC'] = 'galedra2002@gmail.com'
    msg['Subject'] = 'TenderHack fix'

    # second way
    port = 465  # For SSL
    smtp_server = "smtp.mail.ru"
    sender_email = "arsa2003@mail.ru"  # Enter your address
    receiver_email = "arsa2003@mail.ru"  # Enter receiver address
    password = "U3ep7HkJ4ma2UgLqjf1r"
    message = """\
    Subject: Hi, we fixed portal, you can come visit!
    
    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


#send_email()

@shared_task(bind=True)
def send_email_celery(self, user_list: list):
    for user in user_list:
        mail_subject = "Moscow tender portal"
        message = "Portal was fixed"
        to_email = user
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
        return "Done"


mails = ['arsa2003@mail,ru',]
send_email_celery(mails)