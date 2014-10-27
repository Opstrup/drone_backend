"""
docstring for DroneAdmin
All tables in the system can be viewed from the admin
page and manipulated.
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
    docstring for DroneAdmin
    """
    class Meta:
        model = Drone

class UserAdmin(admin.ModelAdmin):
    """
    docstring for UserAdmin
    """
    class Meta:
        model = User

class EventAdmin(admin.ModelAdmin):
    """
    docstring for EventAdmin
    """
    class Meta:
        model = Event

class WaypointAdmin(admin.ModelAdmin):
    """
    docstring for EventAdmin
    """
    class Meta:
        model = Waypoint

class PictureAdmin(admin.ModelAdmin):
    """
    docstring for EventAdmin
    """
    class Meta:
        model = Picture

            
admin.site.register(Event, EventAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Drone, DroneAdmin)
admin.site.register(Waypoint, WaypointAdmin)
admin.site.register(Picture, PictureAdmin)
