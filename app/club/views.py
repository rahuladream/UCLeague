# Python Core import
import os
import datetime
import random
# Django Core Import
from django.http import HttpResponse

# Local imports
from .models import *
import collections


TEAM_SIZE             = 4
ASCII_START_RANGE     = 65
ASCII_END_RANGE       = 91

def random_group(self):

    super_eight_team = [list(team) for team in Team.objects.filter(club_type='SEQ').values_list('club_name','club_state')]
    other_team       = [list(team) for team in Team.objects.filter(club_type='NQ').values_list('club_name','club_state')]
    total_team_size  = len(super_eight_team) + len(other_team)

    if total_team_size % TEAM_SIZE != 0:
        return HttpResponse("Team cannot be formed: Must be Even Number")

    group_count = int(total_team_size / TEAM_SIZE)

    if group_count != len(super_eight_team):
        return HttpResponse('Rules Voileted: Super Eight Qualifiers')

    
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
    
    
    print(groups)


    import json
    return HttpResponse(json.dumps(groups))



