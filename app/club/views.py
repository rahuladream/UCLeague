# Python Core import
import os
import datetime
import random

# Django Core Import
from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

# Local imports
from .models import *
from .constants import *
from .serializers import *

# API Logic Here

__author__ = 'Rahul'

class TeamAPI(APIView):
    serializer_class = TeamSerializer

    def post(self, request, format=None):
        """
        Create a team player
        """
        try:
            data = request.data
            serializer = TeamSerializer(data=data)

            if serializer.is_valid():
                obj = serializer.create(serializer.data)

                return Response({
                    'status': True,
                    'message': 'Team added'
                }, status=status.HTTP_201_CREATED)
            else:
                message = ''
                for error in serializer.errors.values():
                    message += " "
                    message += error[0]
                return Response({
                    'status': False,
                    'message': message
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status': False,
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    



class ListGroupAPI(GenericAPIView):

    def get(self, request):

        """
        List out all the groups in shuffle format
        """

        try:

            super_eight_team = [list(team) for team in Team.objects.filter(club_type='SEQ').values_list('club_name','club_state')]
            other_team       = [list(team) for team in Team.objects.filter(club_type='NQ').values_list('club_name','club_state')]
            total_team_size  = len(super_eight_team) + len(other_team)
            output_group     = []
            if total_team_size % TEAM_SIZE != 0:
                return Response({
                'status': True,
                'message': 'Rules Voileted: Team number mis-matched',
            }, status=status.HTTP_400_BAD_REQUEST)

            group_count = int(total_team_size / TEAM_SIZE)

            if group_count != len(super_eight_team):
                return Response({
                'status': True,
                'message': 'Rules Voileted: Super Eight Qualifiers',
            }, status=status.HTTP_400_BAD_REQUEST)

            def create_team(groups, other_team):
                """
                Creating team of 4 people
                """
                used_team = []
                for i in groups:
                    for team in other_team:
                        if team not in used_team:
                            if len(i[list(i.keys())[0]]['club_state']) == 4:
                                break
                            if team[1] not in i[list(i.keys())[0]]['club_state']:
                                used_team.append(team)
                                i[list(i.keys())[0]]['club_name'].append(team[0])
                                i[list(i.keys())[0]]['club_state'].append(team[1])
                return groups


            while True:
                groups = []
                random.shuffle(super_eight_team)
                random.shuffle(other_team)

                for i in range(group_count):
                    groups.append(
                        {"Group " + chr(ASCII_START_RANGE + i): {
                                'club_name': [super_eight_team[i][0]],
                                'club_state': [other_team[i][1]]
                        }}
                    )
                groups = create_team(groups, other_team)
                border_case = group_count - 1
                if len(groups[i]["Group " + chr(ASCII_START_RANGE + i) ]['club_name']) == 4:
                    break
            
            for i in range(group_count):
                output_group.append({
                "Group " + chr(ASCII_START_RANGE + i): groups[i]["Group "+ chr(ASCII_START_RANGE + i)]['club_name']
            })
            
            return Response({
                'status': True,
                'data': output_group,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': False, 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
    



