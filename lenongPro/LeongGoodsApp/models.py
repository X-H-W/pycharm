from django.db import models
import datetime


# Create your models here.
class TypeInfo(models.Model):
    """商品分类"""
    # 水果类   水产类   肉。。。。。
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle.encode('utf8')


class GoodsInfo(models.Model):
    """商品"""
    gtitle = models.CharField(max_length=20)  # 标题
    gpic = models.ImageField(upload_to='/static/media/')  # 图片
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    gprice = models.DecimalField(max_digits=5, decimal_places=2)  # 价格
    gtype = models.ForeignKey(TypeInfo)  # 商品分类的外间关系
    gclick = models.IntegerField(default=0)
    # gunit = models.CharField(max_length=20,default='500g')# 单位
    gunit = models.IntegerField(default=500)
    gjianjie = models.TextField()
    gpub_date = models.DateTimeField(datetime.datetime.now())
    gpubj_date = models.DateTimeField()

    def __str__(self):
        return self.gtitle.encode('utf8')