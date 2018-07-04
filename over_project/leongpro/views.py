from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo

# Create your views here.
list = []


def register(request):
    return render(request, 'register.html')


def register_handle(request):
    uname = request.POST.get('user_name')
    upwd = request.POST.get('pwd')
    upwd2 = request.POST.get('cpwd')
    uemail = request.POST.get('email')
    user = UserInfo.objects.values_list('uname')
    for i in user:
        
    if uname in list:
        return HttpResponse('已存在')
    else:
        if upwd == upwd2:
            return render(request, 'login.html')
        else:
            return HttpResponse('密码不一致')


def login(request):
    return render(request, 'login.html')
