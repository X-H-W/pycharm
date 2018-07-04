from django.shortcuts import render, redirect
from .models import Banner, About, Project, Case, Tags, Works, Knowledge, About_z, Message
from django.db.models import Q
from django.core.paginator import *


# Create your views here.
# 搜索
def search(request):
    kw = request.POST.get('keywork')
    project_list = Project.objects.filter(Q(name__contains=kw) | Q(contest__contains=kw))
    ctx = {
        'project_list': project_list
    }
    return render(request, 'productlist.html', ctx)


# 主页面
def index(request):
    banner_list = Banner.objects.all()
    about_list = About.objects.all()
    project_list = Project.objects.all()
    case_list = Case.objects.all()

    ctx = {
        'banner_list': banner_list,
        'about_list': about_list,
        'project_list': project_list,
        'case_list': case_list,

    }
    return render(request, 'index.html', ctx)


# 主页面的关于我们
def about(reqeust):
    banner_list = Banner.objects.all()
    tags_list = Tags.objects.all()
    about_list = About_z.objects.all()
    ctx = {
        'banner_list': banner_list,
        'tags_list': tags_list,
        'about_list': about_list
    }
    return render(reqeust, 'about.html', ctx)


# 跳转工程案例
def project_case(request,pindex="1"):
    print(pindex)
    banner_list = Banner.objects.all()
    project_list = Project.objects.all()
    paginator = Paginator(project_list,1)
    page = paginator.page(int(pindex))
    if pindex == '':
        pindex = 1
    ctx = {
        'banner_list': banner_list,
        #'project_list': project_list,
        'page': page

    }
    return render(request, 'productlist.html', ctx)






# 详情
def particulars(request, pid):
    banner_list = Banner.objects.all()
    works_list = Works.objects.all()
    new_project = Project.objects.get(id=pid)
    ctx = {
        'new_project': new_project,
        'banner_list': banner_list,
        'works_list': works_list
    }

    return render(request, 'article_list_content.html', ctx)


def xq(reqeuest, bid):
    banner_list = Banner.objects.all()
    works_list = Works.objects.all()
    case_list = Case.objects.get(id=bid)
    ctx = {
        'banner_list': banner_list,
        'case_list': case_list,
        'works_list': works_list
    }
    return render(reqeuest, '新详情.html', ctx)


def ys(request, tid):
    banner_list = Banner.objects.all()
    knowledge_list = Knowledge.objects.get(id=tid)
    works_list = Works.objects.all()
    ctx = {
        'banner_list': banner_list,
        'knowledge_list': knowledge_list,
        'works_list': works_list
    }
    return render(request, '养生详情.html', ctx)


# 跳转新闻咨询
def news(request):
    banner_list = Banner.objects.all()
    case_list = Case.objects.order_by('-c_time')
    knowledge_list = Knowledge.objects.order_by('-date')
    works_list = Works.objects.all()
    ctx = {
        'banner_list': banner_list,
        'knowledge_list': knowledge_list,
        'works_list': works_list,
        'case_list': case_list
    }
    return render(request, 'article_list.html', ctx)


# 主页的联系我们
def contact(request):
    banner_list = Banner.objects.all()
    ctx = {
        'banner_list': banner_list,
    }
    return render(request, 'contact.html', ctx)


# def mm(request):
#     banner_list = Banner.objects.all()
#     ctx = {
#         'banner_list': banner_list,
#     }
#     return render(request, 'article_list_more.html', ctx)


# def wz(request):
#     banner_list = Banner.objects.all()
#     ctx = {
#         'banner_list': banner_list,
#     }
#     return render(request, 'productdetails.html', ctx)


def messages(request):
    banner_list = Banner.objects.all()
    ctx ={
        'banner_list':banner_list
    }
    return render(request, 'message.html',ctx)


def messages_handle(request):
    banner_list = Banner.objects.all()
    ctx = {
        'banner_list': banner_list
    }

    username = request.POST.get('username', '')
    print(username)
    tel = request.POST.get('tel', '')
    email = request.POST.get('email', '')
    content = request.POST.get('content', '')
    user = Message()
    user.username = username
    user.tel = tel
    user.email = email
    user.content = content
    user.save()
    return render(request, 'message.html',ctx)
