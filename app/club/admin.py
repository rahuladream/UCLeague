# Python Core Import

# Django Core Import
from django.contrib import admin

# Local Import
from .models import *

admin.site.register(Team)
admin.site.register(SaveGroup)