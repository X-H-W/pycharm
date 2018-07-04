from django.shortcuts import render,redirect
from hashlib import sha1
from test1.models import UserInfo,Ima1

# Create your views here.


# 注册页面
def register(request):
    return render(request, 'register.html')


# 登录页面
def login(request):
    return render(request, 'login.html')

def register_handle(request): #注册判断用户输入
    uname = request.POST.get('user_name')
    upwd = request.POST.get('pwd')
    upwd2 = request.POST.get('cpwd')
    uemail = request.POST.get('email')
    filterResult = UserInfo.objects.filter(uname=uname)
    if filterResult:
        return render(request,'存在.html')
    else:
        if upwd == upwd2:
            s1 = sha1()
            s1.update(upwd.encode('utf8'))
            upwd3 = s1.hexdigest()
            UserInfo.objects.create(uname=uname, upwd=upwd3, uemail=uemail)
            return redirect('/user/login')

        else:
            return render(request,'俩次都不一样.html')

def login_handle(request):#登录
    uname = request.POST.get('username')
    upwd = request.POST.get('pwd')
    request.session['uname'] = request.POST['username']

    if upwd:
        s2 = sha1()
        s2.update(upwd.encode('utf8'))
        upwd2 = s2.hexdigest()
        userResult = UserInfo.objects.filter(uname=uname,upwd=upwd2)
        if userResult:
            return redirect('/user/index/')
        else:
            return render(request,'密码错误.html')

def index(request):
    return render(request,'index.html')

