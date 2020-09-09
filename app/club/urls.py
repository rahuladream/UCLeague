# Python core Import
import os

# Django core Import
from django.conf.urls import url

# Local Import
from .views import (
    ListGroupAPI,
    TeamAPI,
    GroupSaveAPI
)

app_name = 'club'

urlpatterns = [
    url(r'team-api/$', TeamAPI.as_view(), name='team-api'),
    url(r'list-group-team/$', ListGroupAPI.as_view(), name='list-group-api'),
    url(r'group-team-save/$', GroupSaveAPI.as_view(), name='save-group-api')


]