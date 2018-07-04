from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime


# Create your models here.
# 轮播图
class Banner(models.Model):
    title = models.CharField('标题', max_length=50)
    cover = models.ImageField('轮播图', upload_to='static/images/banner')
    link_url = models.URLField('图片链接', max_length=100)
    idx = models.IntegerField('索引')
    is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'


# 主页面关于我们
class About(models.Model):
    name = models.CharField('器材名字', max_length=20)
    cover = models.ImageField('器材图片', upload_to='static/images')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '器材关于我们'
        verbose_name_plural = '器材关于我们'


# 工程分类

class Works(models.Model):
    name = models.CharField(verbose_name='分类名称', max_length=500, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


# 工程案例
class Project(models.Model):
    name = models.CharField('工程名字', max_length=20)
    cover = models.ImageField('图片', upload_to='static/images')
    contest = models.TextField('介绍')
    works = models.ForeignKey(Works, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '工程案例'
        verbose_name_plural = '工程案例'


# 主页面的关于我们
class About_z(models.Model):
    name = models.CharField('标题', max_length=30)
    cover = models.ImageField('图片', upload_to='static/images')
    contest = models.TextField('介绍')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '关于我们的主页面'
        verbose_name_plural = verbose_name


# 留言板
class Message(models.Model):
    username = models.CharField('姓名', max_length=30)
    tel = models.CharField('电话', max_length=11)
    email = models.CharField('邮箱', max_length=30)
    content = models.CharField('内容', max_length=500)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '在线留言'
        verbose_name_plural = verbose_name


# 成员
class Tags(models.Model):
    name = models.CharField('名字', max_length=20, default='')
    post = models.CharField('岗位', max_length=20)
    cover = models.ImageField('头像')
    contest = models.CharField('介绍', max_length=50)

    class Meta:
        verbose_name = '成员'
        verbose_name_plural = '成员'

    def __str__(self):
        return self.name


# 新闻质询
class Case(models.Model):
    c_name = models.CharField('标题', max_length=30)
    c_cover = models.ImageField('封面', upload_to='static/images')
    c_contest = models.TextField('内容')
    c_time = models.DateTimeField('时间', default=datetime.now)
    c_works = models.ForeignKey(Works, default='')

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻'

    def __str__(self):
        return self.c_name


# 新闻动态

# class Trends(models.Model):
#     t_name = models.CharField('标题', max_length=30)
#     t_contest = models.TextField('文章')
#
#     class Meta:
#         verbose_name = '新闻动态'
#         verbose_name_plural = '新闻动态'
#
#     def __str__(self):
#         return self.t_name


class Knowledge(models.Model):

    name = models.CharField('标题', max_length=30)
    contest = models.TextField('内容')
    date = models.DateField('日期')
    works = models.ForeignKey(Works, default='')




    class Meta:
        verbose_name = '保护环境(健康)'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
