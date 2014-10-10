"""
Views for backend
These views represents the allowed data to get from the API.
"""

from backend_api.models import Drone, User
from rest_framework import viewsets
from backend_api.serializers import DroneSerializer, UserSerializer

class DroneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
