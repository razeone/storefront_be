"""
URLs file for home module
Cool URIS don't change - Tim Berners Lee
Author: Jorge Raze
"""
from home.views import signup
from django.conf.urls import url

urlpatterns = [
    url(r'^signup/', signup),
]
