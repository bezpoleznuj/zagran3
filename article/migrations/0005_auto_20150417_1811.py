# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_country',
            field=models.CharField(max_length=2, choices=[('HU', 'Угорщина'), ('SK', 'Словаччина')], verbose_name='Країна'),
        ),
    ]
