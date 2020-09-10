# Python core imports
import os
import csv
import json

# django local imports
from app.club.models import *
from django.core.management.base import BaseCommand
from datetime import datetime
from UCLeague.settings import BASE_DIR

class Command(BaseCommand):
    def import_data_group(self):
        data = os.path.join(BASE_DIR, 'app', 'club/management/commands')
        path = data + '/data.json'
        json_path = open(path)
        datas = json.load(json_path)
        
        for data in datas['data']:
            
            try:
                team, created = Team.objects.get_or_create(club_name=data['club_name'],
                                    club_type=data['club_type'],
                                    club_state=data['club_state'],
                                    club_year=data['club_year']
                                    )
                
                if created or team:
                    team.save()
                    display_format = '\n Team, {}, has been saved'
                    print(display_format.format(team))
                

            except Exception as ex:
                        print(str(ex))
                        msg = "\n\nSomething went wrong saving this movie: {}\n{}".format(title, str(ex))
                        print(msg)

        






    def handle(self, *args, **options):
            """
            Call the function to import data
            """
            self.import_data_group()