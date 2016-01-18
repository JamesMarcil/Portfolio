# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=128)),
                ('url', models.SlugField(unique=True)),
                ('authors', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('technology', models.CharField(max_length=255)),
                ('screenshot', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
