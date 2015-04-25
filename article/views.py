from django.shortcuts import render_to_response
from article.models import Article, Image, Contact, Video
from endless_pagination.decorators import page_template
from django.template import RequestContext
# Create your views here.



@page_template("content.html") # just add this decorator

def articles(request,country = '',template="articles.html", extra_context=None):
    if country != '':
        all_articles = Article.objects.filter(article_country = country)
    else:
        all_articles = Article.objects.all()
    context = {
        'objects': all_articles,'contacts':Contact.objects.get(id = 1)
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context,
        context_instance=RequestContext(request))
def article(request, article_id):
    return render_to_response('article.html', {'article': Article.objects.get(id = article_id),'image': Image.objects.filter(image_article_id = article_id),
                                               'video':Video.objects.filter(video_article_id = article_id), 'contacts':Contact.objects.get(id = 1)})