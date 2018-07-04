from django.db import models
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    pub_date = models.DateField(default=0 )
