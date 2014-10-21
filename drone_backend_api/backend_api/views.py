"""
Views for backend
These views represents the allowed data to get from the API.
"""
# pylint: disable=R0904
# pylint: disable=R0901
# pylint: disable=E0602
# pylint: disable=E1101

from backend_api.models import Drone, User, Event
from rest_framework.response import Response
from rest_framework.decorators import api_view
from backend_api.serializers import DroneSerializer, UserSerializer, EventSerializer

@api_view(['GET'])
def user_list(request):
    """
    Method for getting list with all users in the system.
    """
    if request.method == 'GET':
        user = User.objects.all()
        serializer_user = UserSerializer(user, many=True)
        return Response(serializer_user.data)

@api_view(['GET'])
def drone_list(request):
    """
    Method for getting list with all drones in the system.
    """
    if request.method == 'GET':
        drone = Drone.objects.all()
        serializer_drone = DroneSerializer(drone, many=True)
        return Response(serializer_drone.data)

@api_view(['GET', 'PUT'])
def single_drone(request, pk):
    """
    Method for getting single drone.
    Allowed: GET and PUT
    """
    try:
        drone = Drone.objects.get(pk=pk)
    except Drone.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer_drone = DroneSerializer(drone)
        return Response(serializer_drone.data)

    elif request.method == 'PUT':
        serializer_drone = DroneSerializer(drone, data=request.DATA)
        if serializer_drone.is_valid():
            serializer_drone.save()
            return Response(serializer_drone.data)
        return Response(serializer_drone.errors, 
                        status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def event_list(request):
    """
    Method for getting list with all events in the system.
    """
    if request.method == 'GET':
        event = Event.objects.all()
        serializer_event = EventSerializer(event, many=True)
        return Response(serializer_event.data)

@api_view(['GET', 'PUT'])
def single_event(request):
    """
    Method for getting single event.
    Allowed: GET and PUT
    """
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer_event = EventSerializer(event)
        return Response(serializer_event.data)

    elif request.method == 'PUT':
        serializer_event = EventSerializer(event, data=request.DATA)
        if serializer_event.is_valid():
            serializer_event.save()
            return Response(serializer_event.data)
        return Response(serializer_event.errors, 
                        status=status.HTTP_400_BAD_REQUEST)
