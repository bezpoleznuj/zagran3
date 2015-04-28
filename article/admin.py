from django.contrib import admin
from article.models import Article, Image, PlanHouse, PlanArea, Video
from embed_video.admin import AdminVideoMixin
# Register your models here.

class ArticleInLine(admin.StackedInline):
    model = Image
    extra = 1

class VideoInline(AdminVideoMixin, admin.StackedInline):
    model = Video
    extra = 1
    pass
class PlanHouseInLine(admin.StackedInline):
    model = PlanHouse
    extra = 1

class PlanAreaInLine(admin.StackedInline):
    model = PlanArea
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (('Адрес', {'fields': ('article_country', 'article_address')}),(None, {'fields': ('article_short_title','article_text','article_date','article_status','article_price','article_spase','article_rooms','article_floor','article_area','article_walls','article_foto')}),)
    #fields = ('article_short_title','article_text','article_date','article_status','article_price','article_spase','article_rooms','article_floor','article_area','article_walls','article_foto')
    list_display = ['article_country','article_address','article_date', 'article_status']
    list_display_links = ('article_country','article_address', 'article_date','article_status')
    inlines = [ArticleInLine, PlanHouseInLine, PlanAreaInLine, VideoInline]
    list_filter = ['article_date','article_status']
    ordering = ['-article_status']
    search_fields = ['article_address']
admin.site.register(Article, ArticleAdmin)


