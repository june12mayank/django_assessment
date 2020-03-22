## This is in APP/urls.py

from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from notesapi.views import documentViewSet

router = routers.DefaultRouter()
router.register(r'document', DocumentViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]