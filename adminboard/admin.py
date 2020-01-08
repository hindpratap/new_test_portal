from django.contrib import admin
from . models import Authorizedadmin, CreateCandidate, History

admin.site.register([Authorizedadmin, CreateCandidate, History])
