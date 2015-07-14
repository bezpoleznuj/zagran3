from django.db import models
from django.conf import settings
from embed_video.fields import EmbedVideoField
from shutil import copyfile
from datetime import datetime
import os,random,string

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
    article_country = models.CharField('Страна',max_length=2, choices=(('HU', 'Венгрия'),('SK','Словакия')),default='HU')
    article_address = models.CharField('Адрес расположения',max_length=150,blank=True)
    article_short_title = models.TextField('Краткое описание объекта',max_length=300,blank=True)
    article_text = models.TextField('Полное описание объекта',blank=True)

    article_outbuildings = models.TextField('Дополнительные постройки и другие штуки на участке', blank=True)
    article_service = models.TextField('Стоимость коммунальных услуг и их перечень', blank=True)
    article_fence = models.BooleanField('Огражденный Участок или нет',choices=((True, 'Да'),(False,'Нет')),default=True)
    article_date = models.DateTimeField('Дата Создания',default=datetime.now, blank=True )
    article_status = models.BooleanField('Статус объекта',default=True,blank=True, choices=((True, "Продается"),(False,"Продано")))
    article_price = models.CharField('Цена',max_length=15,default=0,blank=True)
    article_spase = models.IntegerField('Площадь',default=0,blank=True)
    article_rooms = models.IntegerField('Количество комнат',default=0,blank=True)
    article_floor = models.IntegerField('Количество этажей',default=1,blank=True)
    article_area = models.CharField('Наличие придомовой территории',max_length=50,blank=True)
    article_walls = models.CharField('Стены',max_length=50,blank=True)
    article_foto = models.ImageField('Фотография объекта', default='',blank=True)
    article_fotosmall = models.ImageField(default='',blank=True)
    article_fotomedium = models.ImageField(default='',blank=True)
    def save(self):
        if self.article_foto.name :
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
            resaize(sname,(160,120))

            copyfile(filename,mname)
            resaize(mname,(400,300))
        else:

            fileName, fileExtension = os.path.splitext('./null.JPG')
            randomname = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(5))
            nullname = fileName+randomname+fileExtension
            nullnameway = os.path.join(settings.MEDIA_ROOT, './null.JPG')
            copyfile(os.path.join(settings.MEDIA_ROOT, './null.JPG'),os.path.join(settings.MEDIA_ROOT, nullname))
            self.article_foto = nullname
            fileName, fileExtension = os.path.splitext(nullname)
            self.article_fotosmall=sname =  fileName+'_s'+fileExtension
            self.article_fotomedium=mname =  fileName+'_m'+fileExtension

            copyfile(nullnameway,os.path.join(settings.MEDIA_ROOT,sname))
            resaize(os.path.join(settings.MEDIA_ROOT,sname),(160,120))

            copyfile(nullnameway,os.path.join(settings.MEDIA_ROOT,mname))
            resaize(os.path.join(settings.MEDIA_ROOT,mname),(400,300))

            super(Article, self).save()

    def article_thumbnail(self):
        if self.article_fotosmall:
            return u'<img src="%s" />' % self.article_fotosmall.url
        else:
            return '(Фотографии нет)'
    article_thumbnail.short_description = 'Фотография'
    article_thumbnail.allow_tags = True

class Image(models.Model):
    class Meta():
        db_table = "Image"
        verbose_name_plural = "Фотография объекта"
    image_article = models.ForeignKey(Article)
    image_foto = models.ImageField('Дополнительное фото объекта',default='')
    def save(self):
        super(Image, self).save()
        resaize(os.path.join(settings.MEDIA_ROOT, self.image_foto.name),(1024,768))

class PlanHouse(models.Model):
    class Meta():
        db_table = 'planhouse'
        verbose_name_plural = "Схема дома"
    planhouse_article = models.ForeignKey(Article)
    planhouse_foto = models.ImageField('План-Схема дома',default='')
    planhouse_foto_s = models.ImageField(default='',blank=True, editable=False)
    def save(self):
        super(PlanHouse, self).save()
        resaize(os.path.join(settings.MEDIA_ROOT, self.planhouse_foto.name),(1024,768))
        fileName, fileExtension = os.path.splitext(self.planhouse_foto.name)
        self.planhouse_foto_s =  fileName+'_s'+fileExtension

        filename = os.path.join(settings.MEDIA_ROOT, self.planhouse_foto.name)

        fileName, fileExtension = os.path.splitext(filename)
        sname = fileName+'_s'+fileExtension

        copyfile(filename, sname)
        resaize(sname,(160,120))
        super(PlanHouse, self).save()

class PlanArea(models.Model):
    class Meta():
        db_table = 'planarea'
        verbose_name_plural = "Схема участка"
    planarea_article = models.ForeignKey(Article)
    planarea_foto = models.ImageField('Схема участка',default='')
    planarea_foto_s = models.ImageField(default='',blank=True,editable=False)
    def save(self):
        super(PlanArea, self).save()
        resaize(os.path.join(settings.MEDIA_ROOT, self.planarea_foto.name),(1024,768))
        fileName, fileExtension = os.path.splitext(self.planarea_foto.name)
        self.planarea_foto_s =  fileName+'_s'+fileExtension

        filename = os.path.join(settings.MEDIA_ROOT, self.planarea_foto.name)

        fileName, fileExtension = os.path.splitext(filename)
        sname = fileName+'_s'+fileExtension

        copyfile(filename, sname)
        resaize(sname,(160,120))
        super(PlanArea, self).save()
class Video(models.Model):
    class Meta():
        db_table = "Video"
        verbose_name_plural = "Видео обзор объекта"
    video_article = models.ForeignKey(Article)
    video = EmbedVideoField()
