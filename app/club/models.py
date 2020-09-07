# Python core Import
import os
import datetime

# Django core import
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local Import
from .constants import *

"""
Model to store the data of teams with year wise
"""

class Team(models.Model):

    club_name       = models.CharField(_('Club Name'), max_length=100)
    club_state      = models.CharField(_('Club State'), max_length=50, choices=STATE_CHOICES)
    club_year       = models.IntegerField(_('Year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    club_type       = models.CharField(_('Club Type'), max_length=20, choices=TEAM_TYPES)


    def __str__(self):
        return self.team_name

