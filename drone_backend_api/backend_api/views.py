"""
This file contains all the views for the drone controle backend.
Views for backend:
These views represents the allowed data to get from the API.
"""
# pylint: disable=R0904
# pylint: disable=R0901
# pylint: disable=E0602
# pylint: disable=E1101

from rest_framework import status
from backend_api.models import Drone, User, Event, Picture, Waypoint
from rest_framework.response import Response
from rest_framework.decorators import api_view
from backend_api.serializers import DroneSerializer, UserSerializer, EventSerializer, PictureSerializer, WaypointSerializer

@api_view(['GET', 'POST'])
def user_list(request):
    """
    Method for getting list with all users in the system
    Allowed: GET and POST
    """
    if request.method == 'GET':
        user = User.objects.all()
        serializer_user = UserSerializer(user, many=True)
        return Response(serializer_user.data)

    elif request.method == 'POST':
        serializer_user = UserSerializer(data=request.DATA)
        if serializer_user.is_valid():
            serializer_user.save()
            return Response(serializer_user.data, status=status.HTTP_201_CREATED)
        return Response(serializer_user.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def drone_list(request):
    """
    Method for getting list with all drones in the system
    Allowed: GET and POST
    """
    if request.method == 'GET':
        drone = Drone.objects.all()
        serializer_drone = DroneSerializer(drone, many=True)
        return Response(serializer_drone.data)

    elif request.method == 'POST':
        serializer_drone = DroneSerializer(data=request.DATA)
        if serializer_drone.is_valid():
            serializer_drone.save()
            return Response(serializer_drone.data, status=status.HTTP_201_CREATED)
        return Response(serializer_drone.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def single_drone(request, pk):
    """
    Method for getting single drone
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
        return Response(serializer_drone.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def event_list(request):
    """
    Method for getting list with all events in the system
    Allowed: GET and POST
    """
    if request.method == 'GET':
        event = Event.objects.all()
        serializer_event = EventSerializer(event, many=True)
        return Response(serializer_event.data)

    elif request.method == 'POST':
        serializer_event = EventSerializer(data=request.DATA)
        if serializer_event.is_valid():
            serializer_event.save()
            return Response(serializer_event.data, status=status.HTTP_201_CREATED)
        return Response(serializer_event.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def single_event(request, pk):
    """
    Method for getting single event
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

@api_view(['GET', 'POST'])
def pictures_list(request):
    """
    List all pictures, or create a new picture
    Allowed: GET and POST
    """
    if request.method == 'GET':
        pictures = Picture.objects.all()
        serializer_pictures = PictureSerializer(pictures, many=True)
        return Response(serializer_pictures.data)

    elif request.method == 'POST':
        serializer_pictures = PictureSerializer(data=request.DATA)
        if serializer_pictures.is_valid():
            serializer_pictures.save()
            return Response(serializer_pictures.data, status=status.HTTP_201_CREATED)
        return Response(serializer_pictures.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def picture_detail(request, pk):
    """
    Detail view of single picture or delete a picture
    Allowed: GET and DELETE
    """
    try:
        picture = Picture.objects.get(pk=pk)
    except Picture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer_pictures = PictureSerializer(picture)
        return Response(serializer_pictures.data)

    elif request.method == 'DELETE':
        picture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def waypoint_list(request):
    """
    List all waypoints, or create a new waypoints
    Allowed: GET and POST
    """
    if request.method == 'GET':
        waypoints = Waypoint.objects.all()
        serializer_waypoints = WaypointSerializer(waypoints, many=True)
        return Response(serializer_waypoints.data)

    elif request.method == 'POST':
        serializer_waypoints = WaypointSerializer(data=request.DATA)
        if serializer_waypoints.is_valid():
            serializer_waypoints.save()
            return Response(serializer_waypoints.data, status=status.HTTP_201_CREATED)
        return Response(serializer_waypoints.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def waypoint_for_event(request, event_id):
    """
    List all waypoint specified to a single waypoint
    Allowed: GET
    """
    try:
        waypoint = Waypoint.objects.all()
    except Waypoint.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        waypoint = waypoint.filter(event_id=event_id)
        serializer_waypoints = WaypointSerializer(waypoint, many=True)
        return Response(serializer_waypoints.data)
