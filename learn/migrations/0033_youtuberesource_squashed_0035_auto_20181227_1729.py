# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-30 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('learn', '0033_youtuberesource'), ('learn', '0034_auto_20181227_1729'), ('learn', '0035_auto_20181227_1729')]

    dependencies = [
        ('learn', '0032_auto_20181217_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_at', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=10000)),
                ('thumbnail_url', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=10)),
                ('view_count', models.IntegerField()),
                ('like_count', models.IntegerField()),
                ('dislike_count', models.IntegerField()),
                ('comment_count', models.IntegerField()),
            ],
        ),
    ]
