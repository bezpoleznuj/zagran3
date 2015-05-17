from django.db import models
from django.conf import settings
from embed_video.fields import EmbedVideoField
from shutil import copyfile
import os
# Create your models here.

def resaize(filename,size=(1024, 768)):
    from PIL import Image
    image = Image.open(filename)
    image.thumbnail(size, Image.ANTIALIAS)
    image.save(filename)

class Article(models.Model):
    class Meta():
        db_table = "article"
        ordering = ["article_order"]
        verbose_name_plural = "Объявления"
    article_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    article_country = models.CharField('Страна',max_length=2, choices=(('HU', 'Венгрия'),('SK','Словакия')))
    article_address = models.CharField('Адрес расположения',max_length=150,default='-')
    article_short_title = models.TextField('Краткое описание объекта',max_length=300,default='-')
    article_text = models.TextField('Полное описание объекта',default='Опис відсутній')
    article_date = models.DateTimeField('Дата Создания')
    article_status = models.BooleanField('Статус объекта',default=True)
    article_price = models.CharField('Цена',max_length=10,default=0)
    article_spase = models.IntegerField('Площадь',default=0)
    article_rooms = models.IntegerField('Количество комнат',default=0)
    article_floor = models.IntegerField('Количество этажей',default=0)
    article_area = models.CharField('Наличие придомовой территории',max_length=50,default='-')
    article_walls = models.CharField('Стены',max_length=50,default='Цегла')
    article_foto = models.ImageField('Фотография объекта', default='')
    article_fotosmall = models.ImageField(default='')
    article_fotomedium = models.ImageField(default='')
    def save(self):
        fileName, fileExtension = os.path.splitext(self.article_foto.name)
        self.article_fotosmall =  fileName+'_s'+fileExtension
        self.article_fotomedium =  fileName+'_m'+fileExtension
        super(Article, self).save()
        filename = os.path.join(settings.MEDIA_ROOT, self.article_foto.name)
        resaize(filename,(1024,768))

        fileName, fileExtension = os.path.splitext(filename)
        sname = fileName+'_s'+fileExtension
        mname = fileName+'_m'+fileExtension

        copyfile(filename, sname)
        resaize(sname,(160,106))

        copyfile(filename,mname)
        resaize(mname,(314,209))

class Image(models.Model):
    class Meta():
        db_table = "Image"
        verbose_name_plural = "фотография объекта"
    image_article = models.ForeignKey(Article)
    image_foto = models.ImageField('Додаткове фото обєкту',default='')
    def save(self):
        super(Image, self).save()
        resaize(os.path.join(settings.MEDIA_ROOT, self.image_foto.name),(1024,768))

class PlanHouse(models.Model):
    class Meta():
        db_table = 'planhouse'
        verbose_name_plural = "Схема дома"
    planhouse_article = models.ForeignKey(Article)
    planhouse_foto = models.ImageField('План-Схема дома',default='')
    def save(self):
        super(PlanHouse, self).save()
        resaize(os.path.join(settings.MEDIA_ROOT, self.planhouse_foto.name),(1024,768))

class PlanArea(models.Model):
    class Meta():
        db_table = 'planarea'
        verbose_name_plural = "Схема участка"
    planarea_article = models.ForeignKey(Article)
    planarea_foto = models.ImageField('Схема участка',default='')
    def save(self):
        super(PlanArea, self).save()
        resaize(os.path.join(settings.MEDIA_ROOT, self.planarea_foto.name),(1024,768))

class Video(models.Model):
    class Meta():
        db_table = "Video"
        verbose_name_plural = "Видео обзор объекта"
    video_article = models.ForeignKey(Article)
    video = EmbedVideoField()