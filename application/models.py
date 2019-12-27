from django.db import models

class Question(models.Model):
    category = models.CharField(max_length=200, null=True, blank=True)
    question = models.TextField(null=True, blank=True)
    option1 = models.TextField(null=True, blank=True)
    option2 = models.TextField(null=True, blank=True)
    option3 = models.TextField(null=True, blank=True)
    option4 = models.TextField(null=True, blank=True)
    option5 = models.TextField(default='null', null=True, blank=True)
    correct = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category


class Tagquestion(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    quesid = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.username