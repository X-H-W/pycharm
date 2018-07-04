from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    a = Blog.objects.all()
    return render(request,'index.html',{'a':a})
