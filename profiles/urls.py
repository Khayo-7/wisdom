from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^abc/$', views.abc),
    url(r'^mob_api/$', views.mobile_api.as_view()),
]