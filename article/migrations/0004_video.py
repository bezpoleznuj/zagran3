# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20150415_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
                ('video_article', models.ForeignKey(to='article.Article')),
            ],
            options={
                'db_table': 'Video',
            },
        ),
    ]
