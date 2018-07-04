from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField('第一个名字', max_length=20)
    last_name = models.CharField('姓',max_length=20)
    emaill = models.CharField('邮箱', max_length=50)
    user_name = models.CharField('用户名', max_length=30)
    password = models.CharField('密码', max_length=20)


    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


# class TestModel(models.Model):
#     title = models.CharField(max_length=50)
#     content = models.TextField()

