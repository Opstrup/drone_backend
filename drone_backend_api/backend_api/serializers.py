"""
Serializer file for backend.
This file contains the classes which provieds the tables attributes
to the rest of the api.
"""
# pylint: disable=w0232
# pylint: disable=R0903
# pylint: disable=C1001
# pylint: disable=C0111


from rest_framework import serializers
from .models import Drone, User, Event, Waypoint, Picture

class DroneSerializer(serializers.ModelSerializer):
    """
    Serializer for the drone table
    """
    class Meta:
        model = Drone
        fields = ('id', 'is_online', 'model',
                  'next_event', 'latitude', 'longitude')

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the user table
    """
    class Meta:
        model = User
        fields = ('id', 'user_name', 'password', 'first_name',
                  'last_name', 'email', 'drone_id')

class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the event table
    """
    class Meta:
        model = Event
        fields = ('id', 'name', 'timestamp', 'updated',
                  'comment', 'error_code', 'drone', 'user')

class WaypointSerializer(serializers.ModelSerializer):
    """
    Serializer for the waypoint table
    """
    class Meta:
        model = Waypoint
        fields = ('id', 'latitude', 'longitude', 'height',
                  'take_photo', 'event_id')

class PictureSerializer(serializers.ModelSerializer):
    """
    Serializer for the picture table
    """
    class Meta:
        model = Picture
        fields = ('id', 'event_id', 'timestamp', 'picture')
