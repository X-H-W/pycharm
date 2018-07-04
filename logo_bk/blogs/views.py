from django.shortcuts import render
from django.views.generic.base import View
from .models import Banner, Post, BlogCategory, FriendlyLink, Comment


# Create your views here.


# def index(request):
#     return render(request,'index.html')

class Index(View):
    def get(self, request):
        # 轮播图
        banner_list = Banner.objects.all()
        # 推荐文章
        recomment_list = Post.objects.filter(recommend=True)
        # 博客分类
        category_list = BlogCategory.objects.all()
        # 取出博客倒序输出
        post_list = Post.objects.order_by('-pub_date')
        # 友情链接
        friendly_list = FriendlyLink.objects.all()
        # 最新评论
        comment_list = Comment.objects.order_by('-pub_date')
        new_comment_list = []
        for t in comment_list:
            if t.post not in new_comment_list:
                new_comment_list.append(t.post)

        ctx = {
            'banner_list': banner_list,
            'recomment_list': recomment_list,
            'category_list': category_list,
            'post_list': post_list,
            'friendly_list': friendly_list,
            'comment_list': comment_list,
        }
        return render(request, 'index.html', ctx)
