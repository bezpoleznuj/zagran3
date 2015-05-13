# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_delete_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['article_order'], 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AddField(
            model_name='article',
            name='article_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
