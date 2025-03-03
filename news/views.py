from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import F, Q
from .models import Article, Tag, Category


"""
Информация в шаблоны будет браться из базы данных
Но пока, мы сделаем переменные, куда будем записывать информацию, которая пойдет в 
контекст шаблона
"""
# Пример данных для новостей

def get_categories_with_news_count():
    """
    Возвращает список категорий с количеством новостей в каждой категории.
    """
    categories = Category.objects.all()
    categories_with_count = []
    for category in categories:
        news_count = Article.objects.filter(category=category).count()
        categories_with_count.append({
            'category': category,
            'news_count': news_count,
        })
    return categories_with_count
info = {
    "users_count": 5,
    "news_count": 10,
    "categories" : Category.objects.all(),
    "menu": [
        {"title": "Главная",
         "url": "/",
         "url_name": "index"},
        {"title": "О проекте",
         "url": "/about/",
         "url_name": "about"},
        {"title": "Каталог",
         "url": "/news/catalog/",
         "url_name": "news:catalog"},
    ],
}

# def get_categories_with_news_count():
#     """
#     Возвращает список категорий с количеством новостей в каждой категории.
#     """
#     categories = Category.objects.all()
#     categories_with_count = []
#     for category in categories:
#         news_count = Article.objects.filter(category=category).count()
#         categories_with_count.append({
#             'category': category,
#             'news_count': news_count,
#         })
#     return categories_with_count
def main(request):
    """
    Представление рендерит шаблон main.html
    """
    categories_with_count = get_categories_with_news_count()
    context = {**info, 'categories_with_count': categories_with_count}
    return render(request, 'main.html', context=context)
   


def about(request):
    """Представление рендерит шаблон about.html"""
    categories_with_count = get_categories_with_news_count()
    context = {**info, 'categories_with_count': categories_with_count }
    return render(request, 'about.html', context=context)


def catalog(request):
    return HttpResponse('Каталог новостей')


def get_categories(request):
    """
    Возвращает все категории для представления в каталоге
    """
    return HttpResponse('All categories')


def get_news_by_category(request, slug):
    """
    Возвращает новости по категории для представления в каталоге
    """
    return HttpResponse(f'News by category {slug}')


def get_news_by_tag(request, slug):
    """
    Возвращает новости по тегу для представления в каталоге
    """
    return HttpResponse(f'News by tag {slug}')


def get_category_by_name(request, slug):
    return HttpResponse(f"Категория {slug}")


def get_all_news(request):
    """Функция для отображения страницы "Каталог"
    будет возвращать рендер шаблона /templates/news/catalog.html
    - **`sort`** - ключ для указания типа сортировки с возможными значениями: `publication_date`, `views`.
    - **`order`** - опциональный ключ для указания направления сортировки с возможными значениями: `asc`, `desc`. По умолчанию `desc`.
    1. Сортировка по дате добавления в убывающем порядке (по умолчанию): `/news/catalog/`
    2. Сортировка по количеству просмотров в убывающем порядке: `/news/catalog/?sort=views`
    3. Сортировка по количеству просмотров в возрастающем порядке: `/news/catalog/?sort=views&order=asc`
    4. Сортировка по дате добавления в возрастающем порядке: `/news/catalog/?sort=publication_date&order=asc`
    """

    # считаем параметры из GET-запроса
    sort = request.GET.get('sort', 'publication_date')  # по умолчанию сортируем по дате загрузки
    order = request.GET.get('order', 'desc')  # по умолчанию сортируем по убыванию

    # Проверяем дали ли мы разрешение на сортировку по этому полю
    valid_sort_fields = {'publication_date', 'views'}
    if sort not in valid_sort_fields:
        sort = 'publication_date'

    # Обрабатываем направление сортировки
    if order == 'asc':
        order_by = sort
    else:
        order_by = f'-{sort}'

    articles = Article.objects.select_related('category').prefetch_related('tags').order_by(order_by)


    paginator = Paginator(articles, 15)
    page = request.GET.get('page')
    paginated_news = paginator.page(paginator.num_pages)
    try:
        paginated_news = paginator.page(page)
    except PageNotAnInteger:
        # Если параметр page не является числом, выводим первую страницу
        paginated_news = paginator.page(1)
    except EmptyPage:
        # Если страница выходит за пределы доступных, выводим последнюю
        paginated_news = paginator.page(paginator.num_pages)
    categories_with_count = get_categories_with_news_count()
    context = {**info,
               'news': paginated_news,
               'news_count': len(articles),

                   }

    return render(request, 'news/catalog.html', context=context)


def get_detail_article_by_id(request, article_id):
    """
    Возвращает детальную информацию по новости для представления
    """
    Article.objects.filter(pk=article_id).update(views=F('views') + 1)
    article = get_object_or_404(Article, id=article_id)

    context = {**info, 'article': article}

    return render(request, 'news/article_detail.html', context=context)


def get_detail_article_by_title(request, title):
    """
    Возвращает детальную информацию по новости для представления
    """

    article = get_object_or_404(Article, slug=title)

    context = {**info, 'article': article}

    return render(request, 'news/article_detail.html', context=context)


def get_articles_by_tag(request, tag_id):

    tag = get_object_or_404(Tag, id=tag_id)
    articles = Article.objects.filter(tags=tag)
    context = {**info, 'news': articles, 'news_count': len(articles), }
    paginator = Paginator(articles, 15)
    page = request.GET.get('page')

    try:
        paginated_news = paginator.page(page)
    except PageNotAnInteger:
        # Если параметр page не является числом, выводим первую страницу
        paginated_news = paginator.page(1)
    except EmptyPage:
        # Если страница выходит за пределы доступных, выводим последнюю
        paginated_news = paginator.page(paginator.num_pages)
    return render(request, 'news/catalog.html', context=context)


def get_articles_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category)
    paginator = Paginator(articles, 15)
    page = request.GET.get('page')

    try:
        paginated_news = paginator.page(page)
    except PageNotAnInteger:
        # Если параметр page не является числом, выводим первую страницу
        paginated_news = paginator.page(1)
    except EmptyPage:
        # Если страница выходит за пределы доступных, выводим последнюю
        paginated_news = paginator.page(paginator.num_pages)
    context = {**info,
               'news': paginated_news,
               'news_count': len(articles),
               'current_category': category,

               }
    return render(request, 'news/catalog.html', context=context)

def search_news(request):
    query = request.GET.get('q')
    articles = Article.objects.all()

    if query:
        # Создаем сложный запрос с использованием Q для поиска в title и content
        articles = articles.filter(
            Q(title__icontains=query) |  # Поиск в заголовке (без учета регистра)
            Q(content__icontains=query)  # Поиск в содержимом (без учета регистра)
        ).distinct()
    paginator = Paginator(articles, 15)
    page = request.GET.get('page')

    try:
        paginated_news = paginator.page(page)
    except PageNotAnInteger:
        # Если параметр page не является числом, выводим первую страницу
        paginated_news = paginator.page(1)
    except EmptyPage:
        # Если страница выходит за пределы доступных, выводим последнюю
        paginated_news = paginator.page(paginator.num_pages)
    context = {
        'news': paginated_news,
        'query': query
    }
    return render(request, 'news/catalog.html', context=context)

