"""
Admin file for drone project
"""

# pylint: disable=R0904
# pylint: disable=R0903
# pylint: disable=w0232
# pylint: disable=C1001
# pylint: disable=C0111

from django.contrib import admin
from .models import Drone, User, Event, Waypoint, Picture

class DroneAdmin(admin.ModelAdmin):
    """
    Drone table
    """
    class Meta:
        model = Drone

class UserAdmin(admin.ModelAdmin):
    """
    User table
    """
    class Meta:
        model = User

class EventAdmin(admin.ModelAdmin):
    """
    Event table
    """
    class Meta:
        model = Event

class WaypointAdmin(admin.ModelAdmin):
    """
    Waypoint table 
    """
    class Meta:
        model = Waypoint

class PictureAdmin(admin.ModelAdmin):
    """
    Picture table
    """
    class Meta:
        model = Picture

            
admin.site.register(Event, EventAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Drone, DroneAdmin)
admin.site.register(Waypoint, WaypointAdmin)
admin.site.register(Picture, PictureAdmin)
