from django.contrib.auth import get_user_model
from celeryproject import settings
from celery import shared_task
from django.core.mail import send_mail
@shared_task(bind=True)
def send_mail_func(self):
    users=get_user_model().objects.all()
    for u in users:
        to_email=u.email

        send_mail(
            'celery hello from django app',
            'message from celery through helo celery',
            settings.EMAIL_HOST_USER,
            [to_email],
            fail_silently=False,
        )

    return "Done"