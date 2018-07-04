from django.conf.urls import include, url
from app1 import views

urlpatterns = [
    url(r'index/',views.index,name='index'),
    url(r'get_handle/',views.get_handle,name='ger_handle')
]