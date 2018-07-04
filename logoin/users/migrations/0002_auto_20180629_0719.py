# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-29 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='emaill',
            field=models.CharField(default='', max_length=50, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=20, verbose_name='姓'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=20, verbose_name='第一个名字'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=20, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='', max_length=30, verbose_name='用户名'),
        ),
    ]