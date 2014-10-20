"""
Serializer file for backend.
This file contains the classes which provieds the tables attributes
to the rest of the api. 
"""

from rest_framework import serializers
from .models import Drone, User

class DroneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drone
        fields = ('id', 'status', 'is_online', 'model', 
                  'next_event', 'latitude', 'longitude')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'password', 'first_name', 
                  'last_name', 'email', 'drone_id')
