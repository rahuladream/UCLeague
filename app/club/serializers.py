#!/usr/bin/env python

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Rest framework imports
from rest_framework import serializers

# Third party Library imports
from .models import *

class ListTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

    def create(self, validated_data):
        return Team.objects.create(**validated_data)
    
    def update(self, validated_data):
        team_obj = Team.objects.get(club_name=validated_data['club_name'])
        return Team.objects.filter(club_name=validated_data['club_name']).update(**validated_data)