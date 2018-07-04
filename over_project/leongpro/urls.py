from django.conf.urls import include, url
from leongpro import views

urlpatterns = [
    url(r'^register/',views.register,name='register'),
    url(r'^register_handle/',views.register_handle,name='register_handle'),
    url(r'^login/',views.login,name='login'),
]