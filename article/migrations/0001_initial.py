# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('article_address', models.CharField(max_length=150, verbose_name='Адреса розташування', default='Адреса відсутня')),
                ('article_short_title', models.TextField(max_length=300, verbose_name='Коротке описання обєкту', default='Короткий опис відсутній')),
                ('article_text', models.TextField(default='Опис відсутній', verbose_name='Повне описання обєкту')),
                ('article_date', models.DateTimeField(verbose_name='Дата Створення')),
                ('article_status', models.BooleanField(default=True, verbose_name='Статус обєкта')),
                ('article_price', models.CharField(max_length=10, verbose_name='Ціна', default=0)),
                ('article_spase', models.IntegerField(default=0, verbose_name='Площа')),
                ('article_rooms', models.IntegerField(default=0, verbose_name='Кількість кімнат')),
                ('article_floor', models.IntegerField(default=0, verbose_name='Кількість поверхів')),
                ('article_area', models.CharField(max_length=50, verbose_name='Наявність прибудинкової території', default='Прибудинкова ділянка відсутня')),
                ('article_walls', models.CharField(max_length=50, verbose_name='Стіни', default='Цегла')),
                ('article_foto', models.ImageField(upload_to='', verbose_name='Фотографія обєкту', default='')),
                ('article_scheme_house', models.ImageField(upload_to='', verbose_name='Схема будинку', default='')),
                ('article_scheme_area', models.ImageField(upload_to='', verbose_name='Схема Ділянки', default='')),
                ('article_country', models.CharField(max_length=20, verbose_name='Країна')),
            ],
            options={
                'ordering': ['article_date'],
                'verbose_name_plural': 'Оголошення',
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('contacts_address', models.CharField(max_length=200)),
                ('contacts_phone', models.CharField(max_length=100)),
                ('contacts_email', models.CharField(max_length=30)),
                ('contacts_guarantees', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Контакти',
                'db_table': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('image_foto', models.ImageField(upload_to='', verbose_name='Додаткове фото обєкту')),
                ('image_article', models.ForeignKey(to='article.Article')),
            ],
            options={
                'db_table': 'Image',
            },
        ),
    ]
