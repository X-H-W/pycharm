# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiuYan',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('uname', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20, default='')),
                ('email', models.CharField(max_length=40, default='')),
                ('address', models.CharField(max_length=40, default='')),
                ('liuyan', models.CharField(max_length=300, default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='uaddress',
        ),
    ]
