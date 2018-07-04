from django.shortcuts import render
from .models import User
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')
def logo(request):
    uname = request.POST.get('First Name','')
    name =request.POST.get('Last Name','')
    email = request.POST.get('Email Address','')
    username=request.POST.get('User Name','')
    passwd = request.POST.get('Password','')
    user = User()
    user.name = uname
    user.last_name = name
    user.emaill = email
    user.user_name = username
    user.password = passwd
    user.save()
    return render(request,'index.html')