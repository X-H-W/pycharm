from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def get_handle(request):
    a = request.GET.get('key1')
    b = request.GET.get('key2')
    c = int(a)+int(b)
    return JsonResponse({'u1':c,'u2':'啦啦啦啦'})