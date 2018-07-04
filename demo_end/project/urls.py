from django.conf.urls import include, url
from project import views

urlpatterns = [
    url(r'^register/',views.register,name='register'),
    url(r'^register_handle/',views.register_handle,name='register_handle'),
    url(r'^login/',views.login,name='login'),
    url(r'login_hadle/',views.login_handle,name='longin_handle'),
    url(r'^logout/',views.logout,name='logout'),
]