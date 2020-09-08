# Python Core import
import os
import datetime
import random
# Django Core Import
from django.http import HttpResponse

# Local imports
from .models import *


# if membersInGroup==4:
#     print("Group {} consists of:".format(group))
#     membersInGroup=0
#     group+=1
# person=random.choice(participants)

# print(person.club_name + " - " + person.club_type + " - " + person.club_state)
# membersInGroup+=1
# participants.remove(person)

TEAM_SIZE             = 4
ASCII_START_RANGE     = 64
ASCII_END_RANGE       = 91

def random_group(self):

    teams             = list(Team.objects.all())
    state             = list(Team.objects.values('club_state').distinct())
    new_team          = list(Team.objects.filter(club_type='NQ'))
    super_eight       = list(Team.objects.filter(club_type='SEQ'))
    total_team_size   = len(new_team) + len(super_eight)
    membersInGroup    = 4    

    if total_team_size % TEAM_SIZE != 0:
        return HttpResponse("Team cannot be formed: Must be Even Number")
    # import pdb; pdb.set_trace()
    team_formed = int(total_team_size / TEAM_SIZE)

    if team_formed != len(super_eight):
        return HttpResponse('Rules Voileted: Super Eight Qualifiers')


    ALL_TEAMS = {}
    for i in range(1, team_formed + 1):
        
        all_state = set()
        single_team = [] 
        choosen_team = random.choice(new_team)
        choosen_super = random.choice(super_eight)
        for j in range(TEAM_SIZE):
            random.shuffle(new_team)
            random.shuffle(super_eight)
            if j == 0:
                all_state.add(choosen_super.club_state)
                single_team.append(choosen_super.club_name)
                super_eight.remove(choosen_super)
            else:
                if choosen_team.club_state not in all_state:
                    single_team.append(choosen_team.club_name)
                    all_state.add(choosen_team.club_state)
                    new_team.remove(choosen_team)
                else:
                    for t in new_team:
                        if t.club_state not in all_state:
                            all_state.add(t.club_state)
                            single_team.append(t.club_name)
                            new_team.remove(t)
                            break;
        print(single_team)
        ALL_TEAMS['Group {}'.format(chr(ASCII_START_RANGE + i))] = single_team
        # ALL_TEAMS.add({ 'Group {}'.format(chr(ASCII_START_RANGE + i)) : list(single_team) })
        
    #     # if _ == 8 and len(single_team) > 4:
    #     #     import pdb; pdb.set_trace()
        
    #     # # if len(single_team) == 3:
    #     # #     import pdb; pdb.set_trace()
    #     # print(len(new_team)) 
        # print(new_team)
        # print(single_team)
    # for key in ALL_TEAMS.items():
    #     print(key)
    import json
    return HttpResponse(json.dumps(ALL_TEAMS))



