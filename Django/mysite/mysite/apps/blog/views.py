from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Article


def start(request):
    return render(request, 'blog/main.html')


def index(request):
    latest_articles_list = Article.objects.order_by('-a_date')[:5]
    return render(request, 'blog/list.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Article Not Found')

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'blog/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Article Not Found')

    a.comment_set.create(auth_name=request.POST['name'], comm_text=request.POST['text'])

    return HttpResponseRedirect( reverse('blog:detail', args= (a.id,)))