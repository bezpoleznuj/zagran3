# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20150415_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_foto',
            field=models.CharField(max_length=200, verbose_name='Фотографія обєкту'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_foto',
            field=models.CharField(max_length=200, verbose_name='Додаткове фото обєкту'),
        ),
    ]
