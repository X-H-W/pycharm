from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    res = HttpResponse
    res.set_cookie(key='t1',value='xuehongwei')
    return res