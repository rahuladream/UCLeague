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

class TeamManager(models.Manager):

    def sequalifiers(self):
        return self.filter(club_type="SEQ")
    
    def nqualifiers(self):
        return self.filter(club_type="NQ")


class Team(models.Model):

    club_name       = models.CharField(_('Club Name'), max_length=100, unique=True)
    club_state      = models.CharField(_('Club State'), max_length=50, choices=STATE_CHOICES)
    club_year       = models.IntegerField(_('Year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    club_type       = models.CharField(_('Club Type'), max_length=20, choices=TEAM_TYPES)

    objects         = TeamManager()

    def __str__(self):
        return self.club_name



class SaveGroup(models.Model):

    group_name      = models.CharField(_('Group Name'), max_length=20)
    team_name       = models.ManyToManyField(Team)
    timestamp       = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.group_name

