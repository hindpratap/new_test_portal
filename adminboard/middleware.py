from datetime import datetime
from adminboard.models import CreateCandidate
from django.contrib.auth.models import User
from django.utils.deprecation import MiddlewareMixin

class RemoveuserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        users = User.objects.exclude(username='raghav').exclude(username='analytics@123')
        for i in users:
            if abs(i.date_joined.date() - datetime.today().date()).days > 14:
                username = i.username
                User.objects.get(username=username).delete()
                candidate = CreateCandidate.objects.get(username=username)
                if candidate.teststatus == 'Pending':
                    candidate.status = 'expired'
                    candidate.save()