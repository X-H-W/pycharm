from django.conf.urls import include, url
from app1 import views

urlpatterns = [
    url(r'^csrf1/$',views.csrf1,name='csrf1'),
    url(r'^csrf2/$',views.csrf2,name='csrf2'),
]
