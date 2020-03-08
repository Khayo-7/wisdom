from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^mob_api/$', views.mobile_api.as_view()),
    url(r'^mob_api/$', views.abc),
]