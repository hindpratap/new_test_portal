from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def sendmailtask(x, y, z):
    send_mail(x, y, settings.EMAIL_HOST_USER, [z])
    return None
