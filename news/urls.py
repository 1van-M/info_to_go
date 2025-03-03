from django.urls import path
from . import views


app_name = 'news'

# будет иметь префикс в urlах /news/
urlpatterns = [
    path('catalog/', views.get_all_news, name='catalog'),
    path('catalog/<int:article_id>/', views.get_detail_article_by_id, name='detail_article_by_id'),
    path('catalog/<slug:title>/', views.get_detail_article_by_title, name='detail_article_by_title'),
    path('articles_by_tag/<int:tag_id>', views.get_articles_by_tag, name='article_by_tag' ),
    path('articles_by_category/<int:category_id>', views.get_articles_by_category, name='article_by_category'),
    path("search_news", views.search_news, name="search_news"),
]
