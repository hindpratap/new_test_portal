from django.db import models
from django.contrib.auth.models import User

class AuthorizedHr(models.Model):
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
    score_reasoning = models.FloatField(null=True, blank=True, default=0)
    score_english = models.FloatField(null=True, blank=True, default=0)
    score_math = models.FloatField(null=True, blank=True, default=0)
    invitestatus = models.CharField(max_length=200, null=True, blank=True, default='Pending')
    teststatus = models.CharField(max_length=200, null=True, blank=True, default='Pending')
    selectionstatus = models.CharField(max_length=200, null=True, blank=True, default='Pending')
    status = models.CharField(max_length=200, null=True, blank=True, default='Pending for invite')
    dob = models.DateField(default=None, null=True, blank=True)
    resume = models.FileField(upload_to='', blank=True)
    created_at = models.DateTimeField(null=True, blank=True, default=None)
    activestatus = models.CharField(max_length=200, null=True, blank=True, default='active')
    source = models.CharField(max_length=200, null=True, blank=True)
    referralid = models.CharField(max_length=100, null=True, blank=True, default='No-referral')
    candempid = models.CharField(max_length=100, null=True, blank=True, default='Nan')
    testcomplete_at = models.DateTimeField(null=True, blank=True, default=None)



    def __str__(self):
        return self.username


class History(models.Model):
    phone = models.BigIntegerField(null=True, blank=True)
    fullname = models.CharField(max_length=300, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    team = models.CharField(max_length=100, null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)
    score_reasoning = models.FloatField(null=True, blank=True, default=0)
    score_english = models.FloatField(null=True, blank=True, default=0)
    score_math = models.FloatField(null=True, blank=True, default=0)
    invitestatus = models.CharField(max_length=200, null=True, blank=True, default='Pending')
    teststatus = models.CharField(max_length=200, null=True, blank=True, default='Pending')
    selectionstatus = models.CharField(max_length=200, null=True, blank=True, default='Pending')
    status = models.CharField(max_length=200, null=True, blank=True, default='Pending for invite')
    dob = models.DateField(default=None, null=True, blank=True)
    resume = models.FileField(upload_to='', blank=True)
    created_at = models.DateTimeField(null=True, blank=True, default=None)
    activestatus = models.CharField(max_length=200, null=True, blank=True, default='active')
    source = models.CharField(max_length=200, null=True, blank=True)
    referralid = models.CharField(max_length=100, null=True, blank=True, default='No-referral')
    candempid = models.CharField(max_length=100, null=True, blank=True, default='Nan')
    updated_at = models.DateTimeField(default=None, blank=True, null=True)
    updated_by = models.EmailField(default=None, blank=True, null=True)



    def __str__(self):
        return self.username


