from django.conf.urls import include, url


urlpatterns = [
    url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^$', 'article.views.articles'),
    url(r'^(?P<country>\w{2})/$', 'article.views.articles'),
]
