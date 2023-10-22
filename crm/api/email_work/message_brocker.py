from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from django_with_celery import settings
@shared_task(bind=True)
def send_mail_func(self):
    #operations
    users = get_user_model().objects.all()
    for user in users:
        mail_subject="Hye from celery"
        message="Yaaaa....I have completed this task by celery!!"
        to_email=user.email
        send_mail(
            subject= mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"