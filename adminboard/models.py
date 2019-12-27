from django.db import models
from django.contrib.auth.models import User

class Authorizedadmin(models.Model):
    email = models.EmailField(null=True)

    def __str__(self):
        return self.email

class CreateCandidate(models.Model):
    phone = models.BigIntegerField(null=True, blank=True)
    fullname = models.CharField(max_length=300, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    team = models.CharField(max_length=100, null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)
    invitestatus = models.CharField(max_length=200, null=True, blank=True, default='Pending')
    teststatus = models.CharField(max_length=200, null=True, blank=True, default='Pending')
    selectionstatus = models.CharField(max_length=200, null=True, blank=True, default='Pending')
    dob = models.DateField(default=None, null=True, blank=True)
    resume = models.FileField(upload_to='', blank=True)
    created_at = models.DateTimeField(null=True, blank=True, default=None)
    activestatus = models.CharField(max_length=200, null=True, blank=True, default='active')


    def __str__(self):
        return self.username

