from django.db import models
from django.conf import settings
from embed_video.fields import EmbedVideoField
# Create your models here.

class Article(models.Model):
    class Meta():
        db_table = "article"
        ordering = ["article_date"]
        verbose_name_plural = "Оголошення"
    article_country = models.CharField('Країна',max_length=2, choices=(('HU', 'Угорщина'),('SK','Словаччина')))
    article_address = models.CharField('Адреса розташування',max_length=150,default='Адреса відсутня')
    article_short_title = models.TextField('Коротке описання обєкту',max_length=300,default='Короткий опис відсутній')
    article_text = models.TextField('Повне описання обєкту',default='Опис відсутній')
    article_date = models.DateTimeField('Дата Створення',)
    article_status = models.BooleanField('Статус обєкта',default=True)
    article_price = models.CharField('Ціна',max_length=10,default=0)
    article_spase = models.IntegerField('Площа',default=0)
    article_rooms = models.IntegerField('Кількість кімнат',default=0)
    article_floor = models.IntegerField('Кількість поверхів',default=0)
    article_area = models.CharField('Наявність прибудинкової території',max_length=50,default='Прибудинкова ділянка відсутня')
    article_walls = models.CharField('Стіни',max_length=50,default='Цегла')
    article_foto = models.CharField('Фотографія обєкту',max_length=200)
    """
    def save(self, size=(1024, 768)):
        from PIL import Image
        
        #Save Photo after ensuring it is not blank.  Resize as needed.
        
        super(Article, self).save()
        filename = settings.MEDIA_ROOT+self.article_foto.name
        image = Image.open(filename)
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(filename)
"""
class Image(models.Model):
    class Meta():
        db_table = "Image"
    image_article = models.ForeignKey(Article)
    image_foto = models.CharField('Додаткове фото обєкту',max_length=200)
    """
    def save(self, size=(1024, 768)):
        from PIL import Image as Image1
        
        #Save Photo after ensuring it is not blank.  Resize as needed.
        
        super(Image, self).save()
        filename = settings.MEDIA_ROOT+self.image_foto.name
        image = Image1.open(filename)
        image.thumbnail(size, Image1.ANTIALIAS)
        image.save(filename)
    """

class Video(models.Model):
    class Meta():
        db_table = "Video"
    video_article = models.ForeignKey(Article)
    video = EmbedVideoField()

class Contact(models.Model):
    class Meta():
        db_table = "contacts"
        verbose_name_plural = "Контакти"
    contacts_address = models.CharField(max_length=200)
    contacts_phone = models.CharField(max_length=100)
    contacts_email = models.CharField(max_length=30)
    contacts_guarantees = models.TextField()
