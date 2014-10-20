"""
Empty doc-string
"""

from .models import Drone, User
from .serializers import DroneSerializer, UserSerializer

from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

class DroneList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        """
        Empty doc-string
        """
        drones = Drone.objects.all()
        serializer_drones = DroneSerializer(drones, many=True)
        return Response(serializer_drones.data)

class UserList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        """
        Empty doc-string
        """
        users = User.objects.all()
        serializer_users = UserSerializer(users, many=True)
        return Response(serializer_users.data)

class SingleDrone(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get_object(self, pk):
        """
        Empty doc-string
        """
        try:
            return Drone.objects.get(pk=pk)
        except Drone.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Empty doc-string
        """
        drone = self.get_object(pk)
        serializer_drone = DroneSerializer(drone)
        return Response(serializer_drone.data)    
