# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20150426_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_foto',
            field=models.ImageField(upload_to='', verbose_name='Додаткове фото обєкту', default=''),
        ),
    ]
