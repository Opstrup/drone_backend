from rest_framework import serializers
#from django.contrib.auth.models import Drone#, User, Event, Waypoint, Picture
#from backend_api.models import Drone#, User, Event, Waypoint, Picture
from backend_api.models import Drone

class DroneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drone
        #fields = ('id', 'status', 'is_online', 'model', 'next_event')
        fields = ('status', 'is_online', 'model', 'next_event')

    # def restore_object(self, attrs, instance=None):
    #     """
    #     Create or update a new snippet instance, given a dictionary
    #     of deserialized field values.

    #     Note that if we don't define this method, then deserializing
    #     data will simply return a dictionary of items.
    #     """
    #     if instance:
    #         # Update existing instance
    #         instance.status = attrs.get('status', instance.status)
    #         instance.is_online = attrs.get('is_online', instance.is_online)
    #         instance.model = attrs.get('model', instance.model)
    #         instance.next_event = attrs.get('next_event', instance.next_event)
    #         return instance

    #     # Create new instance
    #     return DroneBackendApiSerializer(**attrs)
