from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.home),
    url('^index/$', views.index),
]