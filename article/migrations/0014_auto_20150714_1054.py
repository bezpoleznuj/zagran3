# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_remove_planhouse_planhouse_foto_s'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planarea',
            name='planarea_foto_s',
            field=models.ImageField(default='', blank=True, upload_to='', verbose_name='Схема участка'),
        ),
    ]
