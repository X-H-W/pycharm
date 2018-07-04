from django.shortcuts import render, redirect
from . import models
from hashlib import sha1


# Create your views here.
def register(request):
    return render(request, 'register.html')


def register_handle(request):
    # 接收用户输入
    uname = request.POST.get('user_name', '无')
    upwd = request.POST.get('pwd', '无')
    upwd2 = request.POST.get('cpwd', '无')
    uemail = request.POST.get('email', '无')
    # 判断两次密码
    if upwd != upwd2:
        # 如果没有密码不一致 我们就直接重定向返回注册页
        return redirect('/user/register/')
    # 密码加密
    s1 = sha1()
    s1.update(upwd.encode('utf8'))
    upwd3 = s1.hexdigest()

    # 创建模型类对象
    user = models.UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()

    # 注册成功,跳转到登录页面
    return redirect('/user/login/')