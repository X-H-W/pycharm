from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

# 上传图片 安装PILLOW模块
#  配置静态文件路径和modea
class uploadModels(models.Model):
    pic = models.ImageField(upload_to='/static/media/')
    
