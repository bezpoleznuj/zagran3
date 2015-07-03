# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_delete_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': 'Объявления', 'ordering': ['article_order']},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name_plural': 'Фотография объекта'},
        ),
        migrations.AddField(
            model_name='article',
            name='article_fence',
            field=models.BooleanField(default=True, choices=[(True, 'Да'), (False, 'Нет')], verbose_name='Огражденный Участок или нет'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='article_outbuildings',
            field=models.TextField(blank=True, verbose_name='Дополнительные постройки и другие штуки на участке'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_service',
            field=models.TextField(blank=True, verbose_name='Стоимость коммунальных услуг и их перечень'),
        ),
        migrations.AddField(
            model_name='planhouse',
            name='planhouse_foto_s',
            field=models.ImageField(default='', blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_address',
            field=models.CharField(blank=True, max_length=150, verbose_name='Адрес расположения'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_area',
            field=models.CharField(blank=True, max_length=50, verbose_name='Наличие придомовой территории'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_country',
            field=models.CharField(default='HU', verbose_name='Страна', choices=[('HU', 'Венгрия'), ('SK', 'Словакия')], max_length=2),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True, verbose_name='Дата Создания'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_floor',
            field=models.IntegerField(default=1, blank=True, verbose_name='Количество этажей'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_foto',
            field=models.ImageField(default='', blank=True, upload_to='', verbose_name='Фотография объекта'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_fotomedium',
            field=models.ImageField(default='', blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_fotosmall',
            field=models.ImageField(default='', blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_price',
            field=models.CharField(default=0, blank=True, max_length=15, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_rooms',
            field=models.IntegerField(default=0, blank=True, verbose_name='Количество комнат'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_short_title',
            field=models.TextField(blank=True, max_length=300, verbose_name='Краткое описание объекта'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_spase',
            field=models.IntegerField(default=0, blank=True, verbose_name='Площадь'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_status',
            field=models.BooleanField(default=True, choices=[(True, 'Продается'), (False, 'Продано')], verbose_name='Статус объекта'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.TextField(blank=True, verbose_name='Полное описание объекта'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_walls',
            field=models.CharField(blank=True, max_length=50, verbose_name='Стены'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_foto',
            field=models.ImageField(default='', verbose_name='Дополнительное фото объекта', upload_to=''),
        ),
    ]
