# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_data', models.DateTimeField(db_column='pub_data')),
                ('bread', models.IntegerField(default=0)),
                ('bcommet', models.IntegerField(null=True)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HerInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('hname', models.CharField(max_length=10)),
                ('hgender', models.BooleanField(default=True)),
                ('hcontent', models.CharField(max_length=1000)),
                ('isDelete', models.BooleanField(default=False)),
                ('book', models.ForeignKey(to='test1.BookInfo')),
            ],
        ),
    ]
