from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.start, name='start'),
    path('blog/', views.index, name='index'),
    path('adding/', views.adding, name='adding'),
    path('adding/add_article', views.add_article, name='add_article'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)