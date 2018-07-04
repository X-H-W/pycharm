from django.shortcuts import render
import os
from django.conf import settings
from .models import *
from django.http import HttpResponse
# Create your views here.
def index(requset):
    a = GoodsInfo.objects.filter(gtype=1)
    a = a[0:4:1]
    b = GoodsInfo.objects.filter(gtype=9)
    b = b[0:4:1]
    c = GoodsInfo.objects.filter(gtype=10)
    c = c[0:4:1]
    d = GoodsInfo.objects.filter(gtype=11)
    d = d[0:4:1]
    e = GoodsInfo.objects.filter(gtype=12)
    e = e[0:4:1]
    f = GoodsInfo.objects.filter(gtype=13)
    f = f[0:4:1]
    a1 = TypeInfo.objects.filter(id=1)
    a2 = TypeInfo.objects.filter(id=9)
    a3 = TypeInfo.objects.filter(id=10)
    a4 = TypeInfo.objects.filter(id=11)
    a5 = TypeInfo.objects.filter(id=12)
    a6 = TypeInfo.objects.filter(id=13)

    context = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'a1': a1, 'a2': a2, 'a3': a3, 'a4': a4, 'a5': a5,
               'a6': a6}
    return render(requset,'index.html',context)

def cart(request):
    return render(request,'cart.html')

def detail(request,a):
    b = GoodsInfo.objects.filter(id=a)
    return render(request,'detail.html',{'b':b})

def list(request,a):
    if int(a) == 1:
        c = TypeInfo.objects.filter(id=1)
        b = GoodsInfo.objects.filter(gtype=1)
        return render(request, 'list.html', {'b': b, 'a': a,'c':c})
    elif int(a) == 2:
        c = TypeInfo.objects.filter(id=9)
        b = GoodsInfo.objects.filter(gtype=9)
        return render(request, 'list.html', {'b': b, 'a': a,'c':c})
    elif int(a) == 3:
        c = TypeInfo.objects.filter(id=10)
        b = GoodsInfo.objects.filter(gtype=10)
        return render(request, 'list.html', {'b': b, 'a': a,'c':c})

    elif int(a) == 4:
        c = TypeInfo.objects.filter(id=11)
        b = GoodsInfo.objects.filter(gtype=11)
        return render(request, 'list.html', {'b': b, 'a': a,'c':c})

    elif int(a) == 5:
        c = TypeInfo.objects.filter(id=12)
        b = GoodsInfo.objects.filter(gtype=12)
        return render(request, 'list.html', {'b': b, 'a': a,'c':c})

    elif int(a) == 6:
        c = TypeInfo.objects.filter(id=13)
        b = GoodsInfo.objects.filter(gtype=13)
        return render(request, 'list.html', {'b': b, 'a': a,'c':c})
    # return render(request,'list.html')

def place_order(request):
    return render(request,'place_order.html')

def user_center_info(request):
    return render(request,'user_center_info.html')

def user_center_order(request):
    return render(request,'user_center_order.html')

def user_center_site(request):
    return render(request,'user_center_site.html')

def base2(request):
    return render(request,'base2.html')

def base2_handle(request):
    ttitle = request.POST['ttitle']
    gtitle = request.POST['gtitle']
    gprice = request.POST['gprice']
    gunit = request.POST['gunit']
    pic1 = request.FILES.get('gpic')
    picName = os.path.join(settings.MEDIA_ROOT, pic1.name)
    TypeInfo.objects.create(ttitle=ttitle)
    # a = TypeInfo.objects.get(id)
    GoodsInfo.objects.create(gtitle=gtitle,gprice=gprice,gunit=gunit,gpic=picName)
    return HttpResponse('添加成功')
