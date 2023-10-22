from email.utils import formataddr
from email.message import EmailMessage
import smtplib, ssl, csv

from django.core.mail import send_mail, send_mass_mail
from django.contrib.auth import get_user_model
from django.conf import settings

from celery import shared_task
from typing import Union


# @shared_task(bind=True)
def send_email_django(subject: str,
                      user_list: str,
                      message: str):
    #    for user in user_list:
    mail_subject = "Moscow tender portal"
    message_test = "Portal was fixed"
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
