from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('欢迎来到女儿国')
def add(request):
    a = request.GET.get('a','default=123')
    b = request.GET.get('b','default=321')
    c = int(a)+int(b)
    return HttpResponse(str(c))
#def add1(request,a,b):
    #c = int(a)+int(b)
    #return render(request,'home.html',c)

def home(request):
    TutorialList = ['HTML','CSS','jQuery','Python','Django']
    return render(request,'home.html',{'TutorialList':TutorialList})

def home1(request):
    info_dict = {'site':'自强','content':'各种变态'}
    return render(request,'home1.html',{'info_dict':info_dict})
