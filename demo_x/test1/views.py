from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def redTest1(request):
    return HttpResponseRedirect('/redTest2/')


def redTest2(request):
    return HttpResponse('这是调转的页面')