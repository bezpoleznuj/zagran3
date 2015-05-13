from django.db import models
from django.conf import settings
from embed_video.fields import EmbedVideoField

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
        super(Article, self).save()
        filename = settings.MEDIA_ROOT+self.article_foto.name
        resaize(filename,(1024,768))

        f = open(filename,'rb')
        sname = filename[:-4]+'_s'+filename[-4:]
        fcopy = open(sname, 'wb')
        fcopy.write(f.read())
        f.close()
        fcopy.close()
        resaize(fcopy.name,(160,106))

        f = open(filename,'rb')
        sname = filename[:-4]+'_m'+filename[-4:]
        fcopy = open(sname, 'wb')
        fcopy.write(f.read())
        f.close()
        fcopy.close()
        resaize(fcopy.name,(314,209))

        self.article_fotosmall = self.article_foto.name[:-4]+'_s'+self.article_foto.name[-4:]
        self.article_fotomedium = self.article_foto.name[:-4]+'_m'+self.article_foto.name[-4:]
        super(Article, self).save()

class Image(models.Model):
    class Meta():
        db_table = "Image"
        verbose_name_plural = "фотография объекта"
    image_article = models.ForeignKey(Article)
    image_foto = models.ImageField('Додаткове фото обєкту',default='')
    def save(self, size=(1024, 768)):
        super(Image, self).save()
        resaize(settings.MEDIA_ROOT+self.image_foto.name)

class PlanHouse(models.Model):
    class Meta():
        db_table = 'planhouse'
        verbose_name_plural = "Схема дома"
    planhouse_article = models.ForeignKey(Article)
    planhouse_foto = models.ImageField('План-Схема дома',default='')
    def save(self, size=(1024, 768)):
        super(PlanHouse, self).save()
        resaize(settings.MEDIA_ROOT+self.planhouse_foto.name)

class PlanArea(models.Model):
    class Meta():
        db_table = 'planarea'
        verbose_name_plural = "Схема участка"
    planarea_article = models.ForeignKey(Article)
    planarea_foto = models.ImageField('Схема участка',default='')
    def save(self, size=(1024, 768)):
        super(PlanArea, self).save()
        resaize(settings.MEDIA_ROOT+self.planarea_foto.name)

class Video(models.Model):
    class Meta():
        db_table = "Video"
        verbose_name_plural = "Видео обзор объекта"
    video_article = models.ForeignKey(Article)
    video = EmbedVideoField()