from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse
# Create your views here.
def uploadpic(request):
    request.FILES.get('pic1')

    return render(request,'htmlpic.html')

def uploadHandle(request):
    pic1 = request.FILES.get('pic1')
    #
    picName = os.path.join(settings.MEDIA_ROOT,pic1.name)
    with open(picName,'wb') as pic:
        for c in pic1.chunks():
            pic.write(c)
    contest = {'picPath': pic1}
    return render(request,'show.html',contest)
