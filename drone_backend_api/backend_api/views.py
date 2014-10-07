"""
Views for backend
"""

from backend_api.models import Drone
#from django.contrib.auth.models import Drone#, User, Event, Waypoint, Picture
from rest_framework import viewsets
from backend_api.serializers import DroneSerializer

class DroneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
