from email.utils import formataddr
from email.message import EmailMessage
import smtplib, ssl, csv

from django.core.mail import send_mail, send_mass_mail
from django.contrib.auth import get_user_model
from django.conf import settings

from celery import shared_task
from typing import Union


def send_email(user_list):
    # second way
    port = 465  # For SSL
    smtp_server = "smtp.mail.ru"
    sender_email = "arsa2003@mail.ru"  # Enter your address
    receiver_email = ';'.join(user_list)  # Enter receiver address
    password = "U3ep7HkJ4ma2UgLqjf1r"
    message = """\
    Subject: Hi, we fixed portal, you can come visit!
    
    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


# send_email()

# @shared_task(bind=True)
def send_email_django(subject: str,
                      user_list: str):
    #    for user in user_list:
    mail_subject = "Moscow tender portal"
    message = "Portal was fixed"
    send_mail(
        subject=subject,
        message=message,
        from_email='arsa2003@mail.ru',
        recipient_list=user_list.split(','),
        fail_silently=False,
    )
    return "Done"


#mails = ['arsa2003@mail,ru', ]
#(mails)
