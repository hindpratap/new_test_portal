from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def sendmailtask():
    print('going to send')
    send_mail('Hi', 'test', settings.EMAIL_HOST_USER, ['rsharma2@dataflowgroup.com'])
    print('sent successfully')
    return None
