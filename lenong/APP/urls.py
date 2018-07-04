from django.conf.urls import include, url
from django.http import HttpResponse
from . import views


urlpatterns = [
    url(r'^register/$', views.register),
]