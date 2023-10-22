import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

@shared_task
def send_emails(total):
    for i in range(total):
        name = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format()
#        send_email()
    return '{} random users created with success!'.format(total)