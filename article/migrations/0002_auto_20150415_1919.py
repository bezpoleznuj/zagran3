# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_scheme_area',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_scheme_house',
        ),
        migrations.AlterField(
            model_name='article',
            name='article_foto',
            field=models.CharField(default='', verbose_name='Фотографія обєкту', max_length=400),
        ),
    ]
