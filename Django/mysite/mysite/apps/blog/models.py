import datetime

from django.db import models
from django.utils import timezone


class Article(models.Model):
    a_title = models.CharField('Article Name', max_length=200)
    a_text = models.TextField('Article Text')
    a_date = models.DateTimeField('Published on')

    def __str__(self):
        return self.a_title

    def was_published_recently(self):
        return self.a_date >= (timezone.now() - datetime.timedelta(days=7))


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    auth_name = models.CharField('Author', max_length=50)
    comm_text = models.CharField("Text", max_length=200)

    def __str__(self):
        return self.auth_name

