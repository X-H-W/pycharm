from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import RequestContext,loader


#def index(request):
#    r = HttpResponse()
#    r.set_cookie(key='test1',value='xhw')
#    return r

def  index(request):
    # 创建一个HttpRequest对象
    r = HttpResponse()
    # 判断 COOKIE没有 test1 这个账号
    if 'test1' in request.COOKIES:
        # 如果有 赋值给a
        a = request.COOKIES['test1']
        r.write(a)
    return r
