from django.shortcuts import render
from . import models
from django.core.paginator import *


# Create your views here.
def index(request, pindex='1'):
    a = models.HeroInfo.objects.all()
    paginator = Paginator(a, 5)
    page = paginator.page(int(pindex))
    context = {'page': page}
    return render(request, 'index.html', context)
