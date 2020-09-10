# python core impprt

# django core import
from django.test import TestCase

# DRF import
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

# Local imports
from .models import *
from .serializers import *


class ListCreateAPITest(APITestCase):

    def test_list_team(self):
        """
        Ensure that we can list a team member
        """

        client = APIClient()
        url    = '/api/v1/team-api/'
        response = client.get(url)
        data = {'status': True, 'data': []}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)
    

    def test_create_team(self):
        """
        Ensure that the team is created
        """
        team_data = {

        }
        team_serializer = TeamSerializer(data=team_data)

        if team_serializer.is_valid():
            pass
        
        else:
            message = ''
            for error in team_serializer.errors.values():
                message += " "
                message += error[0]
            print(message)
        
        team = Team(**team_data)

        return True
