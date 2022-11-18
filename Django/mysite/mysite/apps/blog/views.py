from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Article


def start(request):
    return render(request, 'blog/main.html')


def index(request):
    latest_articles_list = Article.objects.order_by('-a_date')[:5]
    return render(request, 'blog/list.html', {'latest_articles_list': latest_articles_list})


def adding(request):
    return render(request, 'blog/adding.html')


def add_article(request):
    new_art = Article(a_title=request.POST['name1'], a_text=request.POST['text1'], a_date=timezone.now())
    new_art.save()
    return HttpResponseRedirect(reverse('blog:adding'), {'new_art': new_art})


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

    return HttpResponseRedirect(reverse('blog:detail', args= (a.id,)))

# def add_article(request):
#     method = request.method
#     if method == 'POST':
#         form = forms