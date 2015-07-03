# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20150426_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('planarea_foto', models.ImageField(verbose_name='Схема участка', upload_to='', default='')),
            ],
            options={
                'db_table': 'planarea',
                'verbose_name_plural': 'Схема участка',
            },
        ),
        migrations.CreateModel(
            name='PlanHouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('planhouse_foto', models.ImageField(verbose_name='План-Схема дома', upload_to='', default='')),
            ],
            options={
                'db_table': 'planhouse',
                'verbose_name_plural': 'Схема дома',
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': 'Объявления', 'ordering': ['article_date']},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name_plural': 'фотография объекта'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name_plural': 'Видео обзор объекта'},
        ),
        migrations.AlterField(
            model_name='article',
            name='article_address',
            field=models.CharField(verbose_name='Адрес расположения', max_length=150, default='-'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_area',
            field=models.CharField(verbose_name='Наличие придомовой территории', max_length=50, default='-'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_country',
            field=models.CharField(verbose_name='Страна', choices=[('HU', 'Венгрия'), ('SK', 'Словакия')], max_length=2),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(verbose_name='Дата Создания'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_floor',
            field=models.IntegerField(verbose_name='Количество этажей', default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_foto',
            field=models.ImageField(verbose_name='Фотография объекта', upload_to='', default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_price',
            field=models.CharField(verbose_name='Цена', max_length=10, default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_rooms',
            field=models.IntegerField(verbose_name='Количество комнат', default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_short_title',
            field=models.TextField(verbose_name='Краткое описание объекта', max_length=300, default='-'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_spase',
            field=models.IntegerField(verbose_name='Площадь', default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_status',
            field=models.BooleanField(verbose_name='Статус объекта', default=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.TextField(verbose_name='Полное описание объекта', default='Опис відсутній'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_walls',
            field=models.CharField(verbose_name='Стены', max_length=50, default='Цегла'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacts_address',
            field=models.CharField(verbose_name='Адрес', max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacts_email',
            field=models.CharField(verbose_name='e-mail', max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacts_guarantees',
            field=models.TextField(verbose_name='Гарантия, Лицензия'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacts_phone',
            field=models.CharField(verbose_name='Телефон', max_length=100),
        ),
        migrations.AddField(
            model_name='planhouse',
            name='planhouse_article',
            field=models.ForeignKey(to='article.Article'),
        ),
        migrations.AddField(
            model_name='planarea',
            name='planarea_article',
            field=models.ForeignKey(to='article.Article'),
        ),
    ]
