from django.shortcuts import render
from . import models
from django.core.paginator import Paginator


# Create your views here.
def heroList(request, receive_id):
    List = models.HerInfo.objects.all()
    p = Paginator(List, 5)
    page = p.page(int(receive_id))
    context = {'page': page}
    return render(request, 'heroList.html', context)
