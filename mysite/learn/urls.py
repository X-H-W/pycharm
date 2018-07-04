from django.conf.urls import include, url
from learn import views

urlpatterns = [
    url(r'^index/',views.index),
    url(r'^add/',views.add),
    #url(r'^add/(\d+)/(\d+)/',views.add1,name='add1'),
    url(r'^home/',views.home),
    url(r'^home1/',views.home1)
]