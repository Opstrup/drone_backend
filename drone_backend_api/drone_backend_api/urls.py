"""
URL file for backend_api
"""
# pylint: disable=c0103

from django.conf.urls import url, include, patterns
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('backend_api.views'
                       '',
                       # Frontend urls
                       url(r'^$', 'index_page'),

                       # Admin page url
                       url(r'^admin/', include(admin.site.urls)),

                       # API urls
                       url(r'^api/waypoints/$', 'waypoint_list'),
                       url(r'^api/users/$', 'user_list'),
                       url(r'^api/pictures/$', 'pictures_list'),
                       url(r'^api/pictures/(?P<pk>[0-9]+)/$', 'picture_detail'),
                       url(r'^api/events/$', 'event_list'),
                       url(r'^api/events/(?P<pk>[0-9]+)/$', 'single_event'),
                       url(r'^api/drones/$', 'drone_list'),
                       url(r'^api/drones/(?P<pk>[0-9]+)/$', 'single_drone'),

                       # Authentication url
                       url(r'^api-auth/', include('rest_framework.urls',
                                                  namespace='rest_framework')),
                      )

urlpatterns = format_suffix_patterns(urlpatterns)
