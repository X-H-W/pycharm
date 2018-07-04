from django.db import models


# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=60)
    uemail = models.CharField(max_length=40)
    uaddree = models.CharField(max_length=100)
    uphone = models.IntegerField(max_length=11)
    ureceive = models.CharField(max_length=20)
    uzip_code = models.IntegerField(max_length=6)
    ugender = models.BooleanField(default=False)
