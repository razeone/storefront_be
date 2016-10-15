"""
URLs file for home module
Cool URIS don't change - Tim Berners Lee
Author: Jorge Raze
"""
from .views import register
from django.conf.urls import url

urlpatterns = [
    url(r'^register/', register),
]
