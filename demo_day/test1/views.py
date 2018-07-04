from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def getdata(request):
    return JsonResponse({'u':'你是个好人，恭喜你获得一张好人卡'})