from django.shortcuts import render
from django.conf import settings
import os
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'twoApp/index.html')

def uploadpic(request):
    return render(request)

def show(request):
    a = request.FILES.get('pic')
    pic_url = os.path.join(settings.MEDIA_ROOT.a.name)
    return render(request, 'oneApp/index.html')