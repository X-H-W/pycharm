# @Time    : 18-6-25 下午6:21
# @Author  : xhw
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'index/', views.index, name='index'),
    url(r'about/',views.about,name='about'),
    url(r'project_case/(\d+)', views.project_case, name='project_case'),
    url(r'news/', views.news, name='news'),
    url(r'conteact/', views.contact, name='conteact'),
    url(r'^particulars/(?P<pid>\d+)/',views.particulars,name='particulars'),
    url(r'xq/(?P<bid>\d+)/',views.xq,name='xq'),
    url(r'ys/(?P<tid>\d+)/',views.ys,name='ys'),
    # url(r'mm/',views.mm,name='mm'),
    # url(r'wz/',views.wz,name='wz'),
    url(r'search/',views.search,name='search'),
    url(r'messages/',views.messages,name='messages'),
    url(r'messages_handle/',views.messages_handle,name='messages_handle'),
]
