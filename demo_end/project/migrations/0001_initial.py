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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('uemail', models.CharField(max_length=30)),
                ('ureceive', models.CharField(max_length=20, default='')),
                ('uaddress', models.CharField(max_length=100, default='')),
                ('uzip_code', models.CharField(max_length=6, default='')),
                ('uphone', models.CharField(max_length=11, default='')),
            ],
        ),
    ]