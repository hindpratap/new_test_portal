from django.contrib import admin
from . models import Authorizedadmin, CreateCandidate

admin.site.register([Authorizedadmin, CreateCandidate])
