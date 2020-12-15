from django.conf.urls import patterns, include, url
from rest_framework import routers
from core.views import *

router = routers.DefaultRouter()
router.register(r'cards', CardsViewSet)

urlpatterns = patterns('',
    url(r'', include(router.urls)),
    url(r'^api-auth/$', include('rest_framework.urls', namespace='rest_framework')),
)