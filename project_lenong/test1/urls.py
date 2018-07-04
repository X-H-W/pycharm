from django.conf.urls import include, url
from test1 import views
urlpatterns = [
    url(r'^register/',views.register,name='register'),
    url(r'^login/',views.login,name='login'),
    url(r'^register_handle/',views.register_handle,name='register_handle'),
    url(r'^login_handle/',views.login_handle,name='login_handle'),
    url(r'^index/',views.index,name='index')
]