from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Article


def index(request):
    articles_list = Article.objects.order_by('-date')
    return render(request, 'home/news.html', {'articles_list': articles_list})


def detail(request, id):
    try:
        article = Article.objects.get(id=id)
    except:
        raise Http404('Article not found')

    comment_list = article.comment_set.order_by('-id')[:10]

    return render(request, 'home/detail.html', {'article': article, 'comment_list': comment_list})


def leave_comment(request, id):
    try:
        article = Article.objects.get(id=id)
    except:
        raise Http404('Article not found')

    article.comment_set.create(username='FIXME!', text=request.POST['text'])

    return HttpResponseRedirect(reverse('home:article_detail', args=(article.id,)))