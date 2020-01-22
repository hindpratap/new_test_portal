from django.contrib import admin
from . models import AuthorizedHr, CreateCandidate, History

admin.site.register([AuthorizedHr, CreateCandidate, History])
