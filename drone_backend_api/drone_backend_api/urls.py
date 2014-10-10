"""
URL file for backend_api
"""

from django.conf.urls import url, include
from rest_framework import routers
from backend_api import views

router = routers.DefaultRouter()
router.register(r'drones', views.DroneViewSet)
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
