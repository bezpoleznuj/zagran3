# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20150417_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_fotomedium',
            field=models.ImageField(upload_to='', default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='article_fotosmall',
            field=models.ImageField(upload_to='', default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_foto',
            field=models.ImageField(upload_to='', verbose_name='Фотографія обєкту', default=''),
        ),
    ]
