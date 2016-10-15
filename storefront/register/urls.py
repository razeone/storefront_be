"""
URLs file for home module
Cool URIS don't change - Tim Berners Lee
Author: Jorge Raze
"""
from django.conf.urls import url
from django.conf.urls import include

from django.views.generic import TemplateView

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)

urlpatterns = [
    # url(r'^$', views.RegisterView.as_view(), name='index'),
    url(r'^$', TemplateView.as_view(template_name="register/register.html")),
    url(r'^', include(router.urls)),
    # url(r'^user/', views.CustomerViewSet)
    # url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
]
