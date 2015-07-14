# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_auto_20150714_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planhouse',
            name='planhouse_foto_s',
            field=models.ImageField(blank=True, verbose_name='План-Схема дома', default='', upload_to=''),
        ),
    ]
