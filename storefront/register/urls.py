"""
URLs file for home module
Cool URIS don't change - Tim Berners Lee
Author: Jorge Raze
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.RegisterView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
]