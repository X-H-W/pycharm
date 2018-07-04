from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def csrf1(request):
    return render(request, 'csrf1.html')

@csrf_exempt
def csrf2(request):
    a = request.POST.get('uname')
    return render(request, 'scrf2.html',{'uname':a})

def csrf3(reqeust):
    return render(reqeust,'scrf2.html')
