# Python core Import
import os

# Django core Import
from django.conf.urls import url

# Local Import
from .views import (
    random_group
)


app_name = 'club'

urlpatterns = [
    url(r'random/$', random_group, name='random-group')
]