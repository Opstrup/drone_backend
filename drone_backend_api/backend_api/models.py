"""
Models for the autonomous surveillance drone system.
"""

from django.db import models

class Drone(models.Model):
    """
    Drone table in the database:
    The drone is the hardware unit in the system.
    """
    is_online = models.BooleanField(default=False)
    model = models.CharField(max_length=50, null=True, blank=True)
    next_event = models.IntegerField(null=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

class User(models.Model):
    """
    User table in the database:
    The user table holds all users in the system.
    """
    user_name = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    drone_id = models.ManyToManyField(Drone)

class Event(models.Model):
    """
    Event table in the database:
    The event holds all the information about each flight,
    which drone was out flying, pictures from flight, comments & waypoints.
    Error code holds a number if an error happend during fligth.
    """
    name = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    comment = models.CharField(max_length=100, null=True, blank=True)
    error_code = models.IntegerField(null=True)
    drone = models.ManyToManyField(Drone)
    user = models.ManyToManyField(User)

class Waypoint(models.Model):
    """
    Waypoint table in the database:
    Each waypoint desides actions for the drone,
    has a foreingkey to event.
    """
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    height = models.IntegerField(null=True)
    take_photo = models.BooleanField(default=False)
    event_id = models.ForeignKey(Event)

class Picture(models.Model):
    """
    Picture table in the database:
    Each picture represents a picture taken during flight,
    the pictures is linked to an event via a foreingkey.
    """
    event_id = models.ForeignKey(Event)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    picture = models.ImageField(upload_to='/Users/Opstrup/Documents/projects/drone_backend_api/drone_backend_api/backend_api/static/pictures/')

class  Meta:
    """
    Meta data
    """
    ordering = ('created')
