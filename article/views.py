from django.shortcuts import render_to_response
from article.models import Article, Image, Video, PlanHouse, PlanArea
from endless_pagination.decorators import page_template
from django.template import RequestContext
from constance import config
# Create your views here.

@page_template("content.html")

def articles(request,country = '',template="articles.html", extra_context=None):
    if country != '':
        all_articles = Article.objects.filter(article_country = country)
    else:
        all_articles = Article.objects.all()
    context = {
        'objects': all_articles,
        'config': config,
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context,
        context_instance=RequestContext(request))

def article(request, article_id):
    return render_to_response('article.html', {'article': Article.objects.get(id = article_id),
                                               'image': Image.objects.filter(image_article_id = article_id),
                                               'video':Video.objects.filter(video_article_id = article_id),
                                               'planarea':PlanArea.objects.filter( planarea_article_id = article_id),
                                               'planhouse':PlanHouse.objects.filter( planhouse_article_id = article_id),
                                                'config': config
                                                })