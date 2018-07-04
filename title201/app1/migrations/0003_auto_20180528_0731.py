# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20180528_0716'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LiuYan',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='uaddree',
            field=models.CharField(max_length=100, default='无'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='uliuyan',
            field=models.CharField(max_length=200, default='无'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uemail',
            field=models.EmailField(max_length=40, default='无'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='upwd',
            field=models.CharField(max_length=60),
        ),
    ]
