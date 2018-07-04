from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def a(request):
    return render(request, 'a.html')


def b(request):
    return JsonResponse({'u':'感觉自己萌萌达'})
