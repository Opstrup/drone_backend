"""
docstring for DroneAdmin
"""

from django.contrib import admin

# Register your models here.
from .models import Drone, User

class DroneAdmin(admin.ModelAdmin):
    """
    docstring for DroneAdmin
    """
    class Meta:
        """docstring for Meta"""
        model = Drone

class UserAdmin(admin.ModelAdmin):
    """
    docstring for UserAdmin
    """
    class Meta:
        """docstring for Meta"""
        model = User

            
admin.site.register(User, UserAdmin)
admin.site.register(Drone, DroneAdmin)
