from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_data = models.DateTimeField(db_column='pub_data')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(null=True)
    isDelete = models.BooleanField(default=False)

class HerInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo)