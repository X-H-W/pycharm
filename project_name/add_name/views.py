from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.

def index(request):
    # a = ['python','HTML','CSS']

    # dict = {'name':'张三','age':'18'}

    l = map(str, range(100))

    return render(request, 'home.html', {'dict': l})


def add(request):
    a = request.GET.get('a', '0')
    b = request.GET.get('b', '0')
    c = int(a) + int(b)
    return HttpResponse(c)


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def old_url(requrst, a, b):
    return HttpResponseRedirect(
        reversed('add2', args=(a, b))
    )
