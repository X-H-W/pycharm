# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=60)),
                ('uemail', models.CharField(max_length=40)),
                ('uaddree', models.CharField(max_length=100)),
                ('uphone', models.IntegerField(max_length=11)),
                ('ureceive', models.CharField(max_length=20)),
                ('uzip_code', models.IntegerField(max_length=6)),
                ('ugender', models.BooleanField(default=False)),
            ],
        ),
    ]
