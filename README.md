# Учебный проект "Новости Info to Go"


## Урок 1

### Создали проект `itg`
1. Создали репозиторий
2. Создали проект `itg`
3. Установили зависимости `pip install django`
4. Сохранили зависимости в файл `requirements.txt` командой `pip freeze > requirements.txt`
5. 
Развернуть проект на локальной машине через командную строку:
 - Склонировать репозиторий
 - Перейти в папку проекта
 - Создать виртуальное окружение `python -m venv venv`
 - Активировать виртуальное окружение `source venv/bin/activate` на Linux/MacOS или `.\venv\Scripts\activate.bat` на Windows
 - Установить зависимости `pip install -r requirements.txt`
 - 
Либо через PyCharm:
 - Склонировать репозиторий через File -> Project from Version Control 
 - Установить зависимости через File -> Settings -> Project Interpreter или через `pip install -r requirements.txt` 

### Создание Django project
Создать проект `django-admin startproject itg .`
Этой командой мы создадим проект с именем `itg` в текущей директории.
Точка в конце команды означает, что проект будет создан в текущей директории, 
без создания дополнительной директории с именем проекта.

**commit: `Урок 1: создаём django проект`**

Запуск проекта `python manage.py runserver`
Для запуска проекта, вам нужно использовать терминал, и находясь в директории проекта, на одном уровне с файлом `manage.py`, выполнить команду `python manage.py runserver`
Для остановки сервера используйте комбинацию клавиш `Ctrl+C`

**Команды терминала:**
- `python manage.py runserver` - запуск сервера
- `cd` - смена директории
- `cd..` - переход на уровень выше
- `ls` - просмотр содержимого директории
- `pwd` - показать текущую директорию

**commit: `Урок 1: запускаем django сервер`**

Создание приложения `python manage.py startapp news`
После создания приложения, вам нужно зарегистрировать его в файле `settings.py` в разделе `INSTALLED_APPS`

**commit: `Урок 1: cоздаём django_app news`**

### Создали первое представление
```python
from django.http import HttpResponse
def main(request):
    return HttpResponse("Hello, world!")  # вернет страничку с надписью "Hello, world!"
```

Чтобы представление заработало, его нужно зарегистрировать в файле `urls.py` конфигурации проекта.

### Создали первый URL
```python
from news import views
path('', views.main),
```

Теперь, если вы перейдете на главную страницу сайта, то увидите надпись "Hello, world!"

**commit: `Урок 1: создаём первый маршрут и первое представление`**


## Урок 2

### Создаем детальное представление новости по ее ID
Для этого нам нужно создать новый маршрут, с конвертером `int`, который будет принимать `ID` новости.
```python
path('news/<int:news_id>/', views.news_detail),
```

А так же функцию, которая будет обрабатывать запрос и возвращать страницу с детальной информацией о новости.
```python
def news_by_id(request, news_id):
    return HttpResponse(f"Новость с ID {news_id}")
```

### `include` и собственный файл `urls.py` для приложения `news`
1. Создали еще одно представление `get_all_news` в файле `views.py`
2. Создали файл `urls.py` в директории приложения `news`
3. Зарегистрировали новый файл `urls.py` в файле `urls.py` конфигурации проекта с помощью функции `include`
4. Зарегистрировали маршруты без префикса `news/` в файле `urls.py` приложения `news`

**commit: `Урок 2: собственный urls.py в news и функция include`**

### Знакомство с Django Templates (Шаблоны)
1. Создали папку `templates` в директории приложения `news`
2. Создали файл `catalog.html` в директории `templates/news`
3. Переписали функцию `get_all_news` в файле `views.py` так, чтобы она возвращала страницу `catalog.html`
используя функцию `render` из модуля `django.shortcuts`

**commit: `Урок 2: рендер первого шаблона`**

### Работа с шаблоном 
1. Создали словарь с данными в `views.py` и передали его в шаблон
```python
info = {
    "users_count": 100600,
    "news_count": 1000,
}
```

2. Вставили данные в шаблон `catalog.html` с помощью шаблонного языка `Django Template Language` (`DTL`)

3. Подключили `BS5` по `CDN` и стилизовали страницу

**commit: `Урок 2: передаём первые данные в шаблон и подключил BS5`*


### Смотрим типы данных внутри шаблона

- Проверили, что можно передать только словарь
- Передали список и вывели его в шаблоне
- Передали список меню и познакомились с конструкцией `{% for item in menu %}`
- Познакомились с конструкцией `{% comment %} {% endcomment %}` для комментирования участков шаблона

**commit: `Урок 2: первый цикл в шаблоне`**

### Посмотрели на тег шаблона `if`
Сделали `<hr>` после каждого элемента списка, кроме последнего с помощью специальной переменной `forloop.last`

**commit: `Урок 2: первый тег if в шаблоне`**

### Сделали ссылки в меню кликабельными
- Передали в шаблон список словарей, где каждый словарь содержит `url` и `title`
 
**commit: `Урок 2: сделали ссылки в меню кликабельными`**

- Описали маршруты 
  `/catalog`,
  `/catalog/<int:news_id/>`,
  `/catalog/<slug:slug>`
  и создали соответствующие представления в файле `views.py`
- `catalog` возвращает `HttpResponse("Каталог новостей")`
- `get_news_by_id` возвращает `HttpResponse(f"Новость {news_id}")`
- `get_category_by_name` возвращает `HttpResponse(f"Карточка {slug}")`

**commit: `Урок 2: добавили новые маршруты`**

### Изменение структуры news/url.py` и `news/views.py`
Изменил пути и функции для дальнейшего развития проекта.
Дописали `include` в `urls.py` приложения `itg`

**commit: `Урок 2: изменение структуры путей`**

## Урок 3

### Создание базового шаблона `base.html` в корне проекта в папке `templates`
- Создали базовый шаблон `base.html` в папке `templates`
- Указали кастомный, нестандартный путь для Django в файле `settings.py` в разделе `TEMPLATES` 
- Прописали там `BASE_DIR / 'templates',`
- Подключили базовый шаблон для теста функции `main` в файле `views.py`

**commit: `Урок 3: создали базовый шаблон base.html`**

### Синтаксис блоков в шаблонах. `{% block %}` и `{% extends %}`

- Описали блок `content` в базовом шаблоне `base.html`
- Описали блок `footer` в базовом шаблоне `base.html`
- Создали шаблон `main.html` в папке `templates`, который расширяет базовый шаблон `base.html` через `{% extends %}`
- Переопределили блок `content` в шаблоне `main.html` через `{% block %}`
- Переопределили блок `footer` в шаблоне `main.html` через `{% block %}`
- Подключили шаблон `main.html` в функции `main` в файле `views.py`

**commit: `Урок 3: создали шаблон main.html и расширили базовый шаблон base.html`**

### Создание шаблона `nav_menu.html` и подключение его в базовом шаблоне через `{% include %}`

- Создали каталог `include` в папке `templates` в корне проекта
- Создали шаблон `nav_menu.html` в папке `include`
- Написали навигационное меню в шаблоне `nav_menu.html`
- Использовали шаблонный тег `{% url %}` который позволяет создавать ссылки на страницы по их именам в файле `urls.py`
- Внедрили шаблон `nav_menu.html` в базовый шаблон `base.html` через `{% include %}`
- Добавили датасет с новостями и меню, чтобы в будущем проверить работу шаблона

**commit: `Урок 3: создали шаблон nav_menu.html и внедрили его в базовый шаблон`**

### Начали работу над каталогом новостей (динамическая вставка данных в шаблон, цикл + `include`)

- Создали `include` в папке `templates` в приложении `news`
- Внутри создали шаблон `article_preview.html`
- Шаблон `article_preview.html` пока что только выводит сообщение `hello`
- Подключили шаблон `article_preview.html` в шаблоне `catalog.html` через `{% include %}`

**commit: `Урок 3: начали работу над каталогом новостей и динамической вставкой данных в шаблон`**

- Добавили шаблон `article_detail.html` в папке `templates/news` 
- Доделали `article_preview.html` в папке `templates/news`, распарсив в нём поля `title`, `category`, `tags`, `id_author`, `id_article`, `upload_date`, `views_count`, `favorites_count`
- Те же поля + `content` распарсили в `article_detail.html`
- Обновили функцию `get_detail_article_by_id` - сделали поиск статьи по `id_article` в словаре и возврат шаблона `article_detail.html` ИЛИ `404`

**commit: `Урок 3: доделали каталог новостей и детальное отображение статьи по id_article`**

### Создали папку `static` в приложении `news` и подключили статику в шаблоне `base.html`

- Создали папку `static` в приложении `news`
- Создали папку `news` в папке `static`
- В ней создали папку `css` и файл `main.css`, а так же папку `js` и файл `main.js`
- Создали тестовые стили и скрипт
- Подключили статику в шаблоне `base.html` через тег `{% load static %}` и тег `{% static %}`
- Подключили стили и скрипт в шаблоне `base.html`
- Проверили работу статики на всех страницах
- После создания и подключения статики нужно перезапустить сервер

**commit: `Урок 3: подключили статику в шаблоне base.html`**

### Собственные шаблонные теги через `simple_tag`

- Создали тег шаблона `upper_words` через `simple_tag` в файле `news/templatetags/upper_words.py`
- Протестировали его в представлении `article_detail` в шаблоне `article_detail.html`
- После создания тега и регистрации с помощью `template.Library()` нужно перезапустить сервер

**commit: `Урок 3: создал собственный тег шаблона upper_words через simple_tag`**

### Работа с фильтрами в шаблонах

Посмотрели на работу следующих фильтров в шаблоне `article_preview.html`:
- `length`
- `truncatewords`
- `join`
Так же, в шаблон был добавлен цикл для вывода тегов новости.

**commit: `Урок 3: работа с фильтрами в шаблонах`**


## Урок 4

### Инициализирующие миграции
Применили 18 стартовых миграций для создания структуры БД и настройки
`python manage.py migrate`
Инициализирующая миграция — это первая миграция, которая создается при инициализации нового приложения в Django.
Она содержит начальную структуру базы данных, основанную на моделях, определенных в вашем приложении.
Инициализирующая миграция важна для установления базовой схемы базы данных, с которой будет работать ваше приложение.
`auth`: Миграции для приложения аутентификации, которое включает модели пользователей, групп и разрешений.
`contenttypes`: Миграции для приложения, которое отслеживает типы контента в базе данных.
`sessions`: Миграции для приложения, которое управляет сессиями пользователей.
`admin`: Миграции для административного интерфейса `Django`.

**commit: `Урок 4: применение инициализирующих миграций`**

### Создаём первую модель данных
1. Описание модели
```python
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
```
2. Создание миграции
`python manage.py makemigrations`
3. Применение миграции
`python manage.py migrate`

**commit: `Урок 4: создание модели данных статьи и применение миграции`**

### Знакомство с `Shell Plus` и работа с моделью `Article` в интерактивной оболочке `Django`
- Установили `Shell Plus` командой `pip install django-extensions`
- Добавили `django_extensions` в `INSTALLED_APPS` в файле `settings.py` (перед нашим приложением `news`) 
- Запустили `Shell Plus` командой `python manage.py shell_plus`
(для отображения `SQL` запросов в консоли - `python manage.py shell_plus --print-sql`)
(для выхода из консоли `Shell Plus` - `exit()`)

**commit: `Урок 4: установка Shell Plus и подготовка ORM`**

### Загрузка данных в базу данных из JSON файла
`python manage.py loaddata articles.json`

**commit: `Урок 4: Наполнили базу данных тестовыми данными`**

#### Установили IPython, чтобы прекратить страдания:
```shell
pip install ipython
```
**commit: `Урок 4: установка ipython`**

### Операции CRUD в базе данных
```python
# Откройте Django Shell Plus
python manage.py shell_plus

# Импортируйте модель Article
from news.models import Article

# Создание новой статьи
new_article = Article(
    title="Вода стала розовой!",
    content="Вчера вода во всех реках и озерах стала розовой. Ученые обещают найти причину этого явления.",
    publication_date="2023-10-31T12:00:00Z",
    views=0
)
new_article.save()

# Чтение всех статей
all_articles = Article.objects.all()
for article in all_articles:
    print(article.title, article.content, article.publication_date, article.views)
    
# Чтение одной статьи по её ID
article = Article.objects.get(pk=1)
print(article.title, article.content, article.publication_date, article.views)

# Обновление статьи
article.title = "Обновленная абсурдная новость"
article.content = "Обновленное содержание абсурдной новости"
article.save()

# Удаление статьи
article.delete()
```
**commit: `Урок 4: Посмотрели операции CRUD через командную строку`**


## Урок 5

### Расширили модель данных тегами и категориями через связи `ForeignKey` и `ManyToManyField`
```python
class Article(models.Model):
    ...
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    tags = models.ManyToManyField('Tag', related_name='article')
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
```
### Очистили БД от старых данных с помощью команды `python manage.py flush`
### Создали миграции с помощью команды `python manage.py makemigrations`
### Применили миграции с помощью команды `python manage.py migrate`

**commit: `Урок 5: Добавили модели данных Category и Tag`**

Загрузили новые данные соответствующие новым моделям с помощью команды `python manage.py loaddata articles_2.json`

**commit: `Урок 5: Загрузка новых данных`**

### Рассмотрели примеры в `Django ORM`

```python
# Откройте Django Shell
# python manage.py shell_plus

# Создайте новый тег
new_tag = Tag(name="Новый тег")
new_tag.save()

# Создайте новую категорию
new_category = Category(name="Новая категория")
new_category.save()

# Создайте новую статью с этим тегом и категорией
new_article = Article(
    title="Новая абсурдная новость",
    content="Содержание новой абсурдной новости",
    category=new_category
)
new_article.save()
new_article.tags.add(new_tag)

# Чтение всех категорий
all_categories = Category.objects.all()
for category in all_categories:
    print(category.name)
    
# Чтение всех тегов
all_tags = Tag.objects.all()
for tag in all_tags:
    print(tag.name)
    
# Чтение всех статей
all_articles = Article.objects.all()
for article in all_articles:
    print(article.title, article.content, article.category.name, [tag.name for tag in article.tags.all()])
    
# Чтение одной категории по её ID
category = Category.objects.get(pk=1)
print(category.name)

# Чтение одного тега по его ID
tag = Tag.objects.get(pk=1)
print(tag.name)

# Чтение одной статьи по её ID
article = Article.objects.get(pk=1)
print(article.title, article.content, article.category.name, [tag.name for tag in article.tags.all()])

# Обновите тег
tag = Tag.objects.get(name="Новый тег")
tag.name = "Обновленный тег"
tag.save()

# Обновите категорию
category = Category.objects.get(name="Новая категория")
category.name = "Обновленная категория"
category.save()

# Обновите статью
article = Article.objects.get(title="Новая абсурдная новость")
article.title = "Обновленная абсурдная новость"
article.content = "Обновленное содержание абсурдной новости"
article.save()

# Обновите теги статьи
new_tag = Tag.objects.get(name="Обновленный тег")
article.tags.add(new_tag)

# Удаление категории
category = Category.objects.get(name="Обновленная категория")
category.delete()

# Удаление тега
tag = Tag.objects.get(name="Обновленный тег")
tag.delete()

# Удаление статьи
article = Article.objects.get(title="Обновленная абсурдная новость")
article.delete()
```

**commit: `Урок 5: Посмотрели операции CRUD через командную строку`**

#### Импортировали модели в `news/views.py`
```python
from .models import Article
```

#### Переписали представления для показа каталога новостей и подробного показа новости
```python
def get_all_news(request):
    articles = Article.objects.all()
    context = {
        'news': articles,
        'menu': [
            {"title": "Главная", "url": "/", "url_name": "index"},
            {"title": "О проекте", "url": "/about/", "url_name": "about"},
            {"title": "Каталог", "url": "/news/catalog/", "url_name": "catalog"},
        ],
    }
    return render(request, 'news/catalog.html', context=context)

def get_detail_article_by_id(request, article_id):
    """
    Возвращает детальную информацию по новости для представления
    """
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article,
        'menu': [
            {"title": "Главная", "url": "/", "url_name": "index"},
            {"title": "О проекте", "url": "/about/", "url_name": "about"},
            {"title": "Каталог", "url": "/news/catalog/", "url_name": "catalog"},
        ],
    }
    return render(request, 'news/article_detail.html', context=context)
```

**commit: `Урок 5: Подключили модели данных к представлениям`**

### Сделали ORM запросы на выборку по тегам и категориям

#### Выборка статей по категории

```python
# Пример: Получение всех статей в категории "Технологии"
category_name = "Технологии"
category = Category.objects.get(name=category_name)
articles_in_category = Article.objects.filter(category=category)
for article in articles_in_category:
    print(article.title)
```

#### Выборка статей по тегу
```python
# Пример: Получение всех статей с тегом "Инновации"
tag_name = "Инновации"
tag = Tag.objects.get(name=tag_name)
articles_with_tag = Article.objects.filter(tags=tag)
for article in articles_with_tag:
    print(article.title)
```

#### Выборка статей по категории и тегу
```python
# Пример: Получение всех статей в категории "Наука" и с тегом "Исследования"
category_name = "Наука"
tag_name = "Исследования"
category = Category.objects.get(name=category_name)
tag = Tag.objects.get(name=tag_name)
articles_in_category_and_tag = Article.objects.filter(category=category, tags=tag)
for article in articles_in_category_and_tag:
    print(article.title)
```

**commit: `Урок 5: Посмотрели операции на выборку новостей по тегу и/или категории`**

## Урок 6

### Задача: Получить все статьи, которые принадлежат категории "Технологии".
```python
# Получаем объект категории "Технологии"
technology_category = Category.objects.get(name="Технологии")
# Фильтруем статьи по этой категории
articles_in_technology = Article.objects.filter(category=technology_category)
# Выводим результат
for article in articles_in_technology:
    print(article.title)
```

### Задача: Получить все статьи, которые имеют тег "Инновации".
```python
# Получаем объект тега "Инновации"
innovation_tag = Tag.objects.get(name="Инновации")
# Фильтруем статьи по этому тегу
articles_with_innovation_tag = Article.objects.filter(tags=innovation_tag)
# Выводим результат
for article in articles_with_innovation_tag:
    print(article.title)
```

### Задача: Получить все статьи, отсортированные по заголовку в порядке убывания
```python
# Сортируем статьи по заголовку в порядке убывания
articles_sorted_by_title = Article.objects.all().order_by('-title')
# Выводим результат
for article in articles_sorted_by_title:
    print(article.title, article.id)
```

### Задача: Получить все статьи, у которых количество просмотров больше 10, отсортированные по количеству просмотров в порядке возрастания.
Для начала можно изменить у некоторых статей количество просмотров, чтобы выборка имела смысл
```python
# Фильтруем статьи, у которых id больше 30, и обновляем их количество просмотров
Article.objects.filter(id__gt=30).update(views=20)
```
```python
# Фильтруем статьи по количеству просмотров и сортируем их
articles_filtered_and_sorted = Article.objects.filter(views__gt=10).order_by('views')
# Выводим результат
for article in articles_filtered_and_sorted:
    print(article.title, article.views)
```

**commit: `Урок 6: Рассмотрели операции на фильтрацию и сортировку данных, а так же лукапы`**

### Новое поле `slug` в модели данных `Article`

#### Установка `unidecode`
`pip install unidecode`

#### Сначала нужно очистить БД
`python manage.py flush`

#### Добавляем `slug` и переопределяем метод сохранения
```python
from django.utils.text import slugify
class Article(models.Model):
    ...
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            base_slug = slugify(unidecode.unidecode(self.title))
            self.slug = f"{base_slug}-{self.id}"
        super().save(*args, **kwargs)
```
#### Создаём миграцию
`python manage.py makemigrations`

#### Применяем миграцию
`python manage.py migrate`

#### Загружаем новый дамп данных
`python manage.py loaddata articles_3.json`

#### Проверка работы slugify и unidecode
```python
# Создаем категорию, если она еще не существует
category, created = Category.objects.get_or_create(name="Технологии")

# Создаем теги, если они еще не существуют
tag1, created = Tag.objects.get_or_create(name="Технологии")
tag2, created = Tag.objects.get_or_create(name="Инновации")

# Создаем статью
article = Article(
    title="Новая статья о технологиях",
    content="Это тестовая статья для проверки работы поля slug.",
    category=category,
)

# Сохраняем статью, чтобы убедиться, что slug был сгенерирован
article.save()

# Добавляем теги к статье
article.tags.add(tag1, tag2)

# Выводим информацию о статье, чтобы убедиться, что slug был сгенерирован
print(f"Title: {article.title}")
print(f"Slug: {article.slug}")
print(f"Content: {article.content}")
print(f"Category: {article.category.name}")
print(f"Tags: {', '.join([tag.name for tag in article.tags.all()])}")
```

**commit: `Урок 6: Добавили slug в Article`**

### Добавление слага в маршруты и представления
```python
# news/urls.py
urlpatterns = [
    ...
    path('catalog/<slug:slug>/', views.get_detail_article_by_slag, name='detail_article_by_slag'),
]
```
```python
# news/views.py
def get_detail_article_by_slag(request, slug):
    article = get_object_or_404(Article, slug=slug)
    ...
    return render(request, 'news/article_detail.html', context=context)
```

**commit: `Урок 6: Добавление slug в маршруты и представления`**


## Урок 7

### Очистка базы данных
`python manage.py flush`

### Загрузка новых данных
`python manage.py loaddata articles_4.json`

**commit: `Урок 7: Подготовка данных`**

### Класс Q
```python
# Пример 1: Простое использование Q
# Создаем объекты Q для условий
category_q = Q(category__name='Технологии')
tag_q = Q(tags__name='Инновации')
# Комбинируем условия с помощью логического оператора OR
articles = Article.objects.filter(category_q | tag_q)

# Пример 2: Комбинирование условий с AND и OR
# Создаем объекты Q для условий
category_q = Q(category__name='Наука')
tag_q1 = Q(tags__name='Исследования')
tag_q2 = Q(tags__name='Инновации')
# Комбинируем условия с помощью логических операторов
articles = Article.objects.filter(category_q & (tag_q1 | tag_q2))

# Пример 3: Использование NOT
# Создаем объект Q для условия
category_q = Q(category__name='Спорт')
# Используем логический оператор NOT
articles = Article.objects.filter(~category_q)

# Пример 4: Комбинирование нескольких условий
# Создаем объекты Q для условий
category_q1 = Q(category__name='Технологии')
category_q2 = Q(category__name='Наука')
tag_q1 = Q(tags__name='Инновации')
tag_q2 = Q(tags__name='Исследования')
# Комбинируем условия с помощью логических операторов
articles = Article.objects.filter((category_q1 | category_q2) & (tag_q1 | tag_q2))
```
**commit: `Урок 7: Класс Q`**

### Методы exists() и count(): Проверка наличия данных и подсчёт записей
```python
# Пример 1: Проверка наличия статей в категории "Технологии"
# Проверяем наличие статей в категории "Технологии"
exists = Article.objects.filter(category__name='Технологии').exists()
print(exists)  # Выведет True или False

# Пример 2: Подсчет количества статей в категории "Наука"
# Подсчитываем количество статей в категории "Наука"
count = Article.objects.filter(category__name='Наука').count()
print(count)  # Выведет количество статей

# Пример 3: Проверка наличия статей с тегом "Инновации" или "Исследования"
# Создаем объекты Q для условий
tag_q1 = Q(tags__name='Инновации')
tag_q2 = Q(tags__name='Исследования')
# Проверяем наличие статей с тегами "Инновации" или "Исследования"
exists = Article.objects.filter(tag_q1 | tag_q2).exists()
print(exists)  # Выведет True или False

# Пример 4: Подсчет количества статей в категории "Технологии" или "Наука"
# Создаем объекты Q для условий
category_q1 = Q(category__name='Технологии')
category_q2 = Q(category__name='Наука')
# Подсчитываем количество статей в категории "Технологии" или "Наука"
count = Article.objects.filter(category_q1 | category_q2).count()
print(count)  # Выведет количество статей
```
**commit: `Урок 7: Методы exists() и count()`**

### Класс F, Value и метод annotate(): Выполнение операций с полями внутри запросов

```python
# Пример 1: Увеличение количества просмотров статьи
# Найдем статью по slug и увеличим количество просмотров на 1
Article.objects.filter(slug='17-kroty-otkryli-restoran').update(views=F('views') + 1)

# Пример 2: Аннотация статей с константным значением
# Аннотируем все статьи с константным значением is_featured
articles = Article.objects.annotate(is_featured=Value(True))
for article in articles:
    print(article.is_featured)  # Выведет True для всех статей
    
# Пример 3: Аннотация статей с количеством просмотров, увеличенным на 10
# Аннотируем все статьи с количеством просмотров, увеличенным на 10
articles = Article.objects.annotate(increased_views=F('views') + 10)
for article in articles:
    print(article.increased_views)  # Выведет количество просмотров, увеличенное на 10
```
**commit: `Урок 7: Класс F, Value и метод annotate()`**

### Агрегация данных: Использование Count, Sum, Avg, Max, Min и метода values()
```python
# Пример 1: Подсчет количества статей в каждой категории
# Подсчитываем количество статей в каждой категории
category_counts = Article.objects.values('category__name').annotate(count=Count('id'))
for category in category_counts:
    print(f"Category: {category['category__name']}, Count: {category['count']}")
    
# Пример 2: Суммирование количества просмотров всех статей
# Подсчитываем суммарное количество просмотров всех статей
total_views = Article.objects.aggregate(total_views=Sum('views'))
print(f"Total Views: {total_views['total_views']}")

# Пример 3: Вычисление среднего количества просмотров статей
# Вычисляем среднее количество просмотров статей
average_views = Article.objects.aggregate(average_views=Avg('views'))
print(f"Average Views: {average_views['average_views']}")

# Пример 4: Нахождение максимального и минимального количества просмотров статей
# Находим максимальное и минимальное количество просмотров статей
max_views = Article.objects.aggregate(max_views=Max('views'))
min_views = Article.objects.aggregate(min_views=Min('views'))
print(f"Max Views: {max_views['max_views']}")
print(f"Min Views: {min_views['min_views']}")

# Пример 5: Подсчет количества статей в каждой категории с использованием values() и annotate()
# Подсчитываем количество статей в каждой категории
category_counts = Article.objects.values('category__name').annotate(count=Count('id'))
for category in category_counts:
    print(f"Category: {category['category__name']}, Count: {category['count']}")
```
**commit: `Урок 7: Агрегация данных`**

- установили отладочную панель `Django` (`pip install django-debug-toolbar`) и настроили её
- убедились в том, что наше приложение генерирует слишком много запросов

**commit: `Урок 7: Установили отладочную панель Django`**

#### включили жадную загрузку и снизили количество запросов до 4
```python
articles = Article.objects.select_related('category').prefetch_related('tags')
```

### `prefetch_related` и `select_related`
`prefetch_related` и `select_related` — это методы оптимизации запросов в `Django ORM`,
которые используются для уменьшения количества запросов к базе данных и повышения производительности при работе с моделями,
связанными через внешние ключи или отношения "многие ко многим".

#### `select_related`
`select_related` используется для выполнения запросов к моделям, связанных через внешние ключи (`ForeignKey`).
Это позволяет получить все необходимые данные за один запрос,
вместо того чтобы выполнять отдельные запросы для каждого связанного объекта.

#### `prefetch_related`
`prefetch_related` используется для выполнения отдельных запросов для получения связанных объектов,
но делает это более эффективно, чем выполнение отдельных запросов для каждого связанного объекта.
Это особенно полезно для отношений "многие ко многим" (`ManyToManyField`) и обратных отношений (`reverse ForeignKey`).

#### Основные различия
1. **Тип отношений**:
   - `select_related` работает с однозначными отношениями (`ForeignKey` и `OneToOneField`).
   - `prefetch_related` работает с отношениями "многие ко многим" (`ManyToManyField`) и обратными отношениями (`reverse ForeignKey`).
2. **Механизм работы**:
   - `select_related` использует `SQL`-объединения (`JOIN`), что может быть более эффективно для небольших наборов данных.
   - `prefetch_related` выполняет отдельные запросы для получения связанных объектов, что может быть более эффективно для больших наборов данных или сложных отношений.
3. **Производительность**:
   - `select_related` может быть быстрее для небольших наборов данных, так как выполняет меньше запросов.
   - `prefetch_related` может быть более эффективен для больших наборов данных, так как выполняет отдельные запросы для связанных объектов, что может уменьшить нагрузку на базу данных.

### Ленивая загрузка (`Lazy Loading`) и Жадная загрузка (`Eager Loading`)
В `Django ORM` ленивая загрузка (`lazy loading`) и жадная загрузка (`eager loading`) — это два подхода к загрузке связанных данных, которые могут существенно повлиять на производительность вашего приложения. Выбор между ними зависит от конкретных требований и сценариев использования.

#### Ленивая загрузка (`Lazy Loading`)
Ленивая загрузка — это подход, при котором связанные данные загружаются только тогда, когда они действительно нужны.
Это поведение по умолчанию в `Django ORM`.
**Преимущества:**
- **Экономия ресурсов:** Данные загружаются только при необходимости, что может снизить нагрузку на базу данных и уменьшить использование памяти.
- **Простота:** Не требует дополнительных настроек или оптимизаций.
**Недостатки:**
- **N+1 проблема:** Может привести к большому количеству запросов к базе данных, если связанные данные загружаются в цикле.
**Пример:**
```python
articles = Article.objects.all()
for article in articles:
    print(article.title)  # Каждый раз выполняется отдельный запрос для получения статьи
```

#### Жадная загрузка (`Eager Loading`)
Жадная загрузка — это подход, при котором связанные данные загружаются заранее, в один или несколько запросов.
В `Django` это достигается с помощью методов `select_related` и `prefetch_related`.
**Преимущества:**
- **Снижение количества запросов:** Уменьшает количество запросов к базе данных, что может значительно повысить производительность.
- **Оптимизация:** Позволяет более эффективно использовать ресурсы базы данных и памяти.
**Недостатки:**
- **Избыточность:** Может загружать данные, которые в итоге не понадобятся, что может привести к избыточному использованию памяти.
- **Сложность:** Требует дополнительных настроек и оптимизаций.
**Пример с `select_related` и `prefetch_related`:**
```python
articles = Article.objects.select_related('category').prefetch_related('tags')
for article in articles:
    print(article.title)  # Все книги загружены заранее, один запрос к базе данных для category и несколько для tags
```

#### Когда использовать ленивую загрузку
- **Простые запросы:** Когда вы знаете, что связанные данные будут загружаться редко или только для небольшого числа объектов.
- **Малые наборы данных:** Когда работаете с небольшими наборами данных, где дополнительные запросы не будут существенно влиять на производительность.
- **Прототипирование:** На этапе разработки и тестирования, когда производительность не является критичной.

#### Когда использовать жадную загрузку
- **Сложные запросы:** Когда вы знаете, что будете часто обращаться к связанным данным, особенно в циклах.
- **Большие наборы данных:** Когда работаете с большими наборами данных, где множество отдельных запросов могут существенно замедлить выполнение.
- **Производительность:** В производственных системах, где производительность критична и необходимо минимизировать количество запросов к базе данных.

Выбор между ленивой и жадной загрузкой зависит от конкретных требований вашего приложения.
Ленивая загрузка проще в использовании и может быть достаточной для простых сценариев,
тогда как жадная загрузка требует дополнительных настроек,
но может значительно повысить производительность в сложных и ресурсоёмких запросах.

**commit: `Урок 7: включили жадную загрузку`**


## Урок 8

### Немного об SQL
`SQL` (`Structured Query Language`) — это стандартный язык для работы с реляционными базами данных. Он позволяет выполнять различные операции, такие как создание, изменение, удаление и извлечение данных.

#### Основные команды SQL:
- **SELECT**: Извлечение данных из базы данных.
- **INSERT**: Добавление новых данных в таблицу.
- **UPDATE**: Обновление существующих данных в таблице.
- **DELETE**: Удаление данных из таблицы.
- **CREATE**: Создание новых таблиц или баз данных.
- **ALTER**: Изменение структуры существующей таблицы.
- **DROP**: Удаление таблицы или базы данных.

#### Примеры использования:
- **SELECT**: `SELECT * FROM users;`
- **INSERT**: `INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');`
- **UPDATE**: `UPDATE users SET email = 'newemail@example.com' WHERE name = 'John Doe';`
- **DELETE**: `DELETE FROM users WHERE name = 'John Doe';`
`SQL` является мощным инструментом для управления данными и используется в различных системах управления базами данных (СУБД), таких как `PostgreSQL`, `MySQL`, `Oracle` и другие.

**commit: `Урок 8: немного об SQL`**

### Основные возможности pgAdmin: Управление базой данных и визуализация
`pgAdmin` — это мощный инструмент для управления базами данных `PostgreSQL`, который предоставляет широкий спектр возможностей для администрирования и визуализации данных.

#### Основные возможности:
- **Управление базой данных**: Создание, изменение и удаление баз данных, таблиц, индексов, представлений и других объектов.
- **Визуализация данных**: Графическое представление структуры базы данных, визуализация запросов и результатов выполнения.
- **Мониторинг и управление производительностью**: Мониторинг и управление производительностью базы данных.
- **Управление пользователями и ролями**: Настройка прав доступа и управление пользователями.

#### Примеры использования:
- **Создание таблицы**: Используйте графический интерфейс для создания новых таблиц.
- **Выполнение запросов**: Используйте вкладку "Query Tool" для выполнения SQL-запросов.
- **Визуализация данных**: Построение диаграмм и отчетов на основе данных.
`pgAdmin` позволяет эффективно управлять базами данных `PostgreSQL`, обеспечивая удобный и интуитивно понятный интерфейс для выполнения различных задач.

**commit: `Урок 8: основные возможности pgAdmin: Управление базой данных и визуализация`**

### Создание таблиц: Структура и параметры таблиц
Создание таблиц в `PostgreSQL` — это процесс определения структуры данных, которые будут храниться в базе данных. Вот пошаговое руководство по созданию таблиц:

#### Шаги создания таблицы:
1. **Откройте pgAdmin и подключитесь к серверу**.
2. **Выберите базу данных**.
3. **Создайте новую таблицу**:
   - Щелкните правой кнопкой мыши на базе данных и выберите "Create" -> "Table".
   - Введите имя таблицы и выберите схему (по умолчанию `public`).
4. **Определите столбцы**:
   - В разделе "Columns" добавьте столбцы, указав их имена, типы данных и ограничения (например, `NOT NULL`, `UNIQUE`).
5. **Сохраните таблицу**:
   - Нажмите "Save" для создания таблицы.

#### Параметры таблиц:
- **Типы данных**: Определяют, какие данные могут храниться в столбцах (например, `INTEGER`, `VARCHAR`, `DATE`).
- **Ограничения**: Ограничения, такие как `NOT NULL`, `UNIQUE`, `CHECK`, которые обеспечивают целостность данных.
- **Индексы**: Структуры, которые ускоряют поиск данных.
- **Внешние ключи**: Ссылки на первичные ключи в других таблицах, которые устанавливают связи между таблицами.

#### Пример создания таблицы:
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

**commit: `Урок 8: cоздание таблиц: Структура и параметры таблиц`**

### Типы данных: Основные типы данных `PostgreSQL`
`PostgreSQL` поддерживает широкий спектр типов данных, которые могут быть использованы для хранения различных видов информации. Вот список основных типов данных и их применения:

#### Числовые типы:
- **INTEGER**: Целое число. Используется для хранения целых чисел, таких как идентификаторы, количества и т.д.
- **BIGINT**: Большое целое число. Используется для хранения очень больших целых чисел.
- **SMALLINT**: Малое целое число. Используется для хранения небольших целых чисел.
- **NUMERIC (или DECIMAL)**: Число с фиксированной точностью. Используется для хранения денежных сумм, процентов и других точных чисел.
- **REAL**: Число с плавающей точкой одинарной точности. Используется для хранения чисел с плавающей точкой, где точность не критична.
- **DOUBLE PRECISION**: Число с плавающей точкой двойной точности. Используется для хранения чисел с плавающей точкой, где требуется высокая точность.
- **SERIAL**: Автоинкрементное целое число. Используется для создания уникальных идентификаторов.

#### Строковые типы:
- **CHAR(n)**: Фиксированная длина строки. Используется для хранения строк фиксированной длины.
- **VARCHAR(n)**: Переменная длина строки. Используется для хранения строк переменной длины.
- **TEXT**: Строка переменной длины без ограничения. Используется для хранения больших объемов текста.

#### Дата и время:
- **DATE**: Дата. Используется для хранения дат без времени.
- **TIME**: Время. Используется для хранения времени без даты.
- **TIMESTAMP**: Дата и время. Используется для хранения даты и времени.
- **TIMESTAMPTZ**: Дата и время с часовым поясом. Используется для хранения даты и времени с учетом часового пояса.
- **INTERVAL**: Интервал времени. Используется для хранения промежутков времени.

#### Логические типы:
- **BOOLEAN**: Логическое значение. Используется для хранения значений `TRUE` или `FALSE`.

#### Двоичные типы:
- **BYTEA**: Двоичные данные. Используется для хранения двоичных данных, таких как изображения, файлы и т.д.

#### Специальные типы:
- **UUID**: Универсальный уникальный идентификатор. Используется для хранения уникальных идентификаторов.
- **JSON**: JSON данные. Используется для хранения данных в формате JSON.
- **JSONB**: Двоичный JSON. Используется для хранения данных в формате JSON с более эффективным хранением и поиском.
- **ARRAY**: Массив. Используется для хранения массивов данных.
- **ENUM**: Перечисление. Используется для хранения значений из заранее определенного набора.

**commit: `Урок 8: типы данных: Основные типы данных PostgreSQL`**

### Проектирование моделей баз данных: Оптимизация структуры базы данных для типичных задач
Проектирование базы данных — это процесс создания структуры базы данных, которая эффективно хранит, извлекает и управляет данными. Основные шаги проектирования базы данных включают:
#### Этапы проектирования базы данных:
1. **Сбор требований**: Определение, какие данные нужно хранить и как они будут использоваться.
2. **Концептуальное проектирование**: Создание ER-диаграмм (Entity-Relationship) для визуализации сущностей и их связей.
3. **Логическое проектирование**: Определение таблиц, столбцов, типов данных и ограничений.
4. **Физическое проектирование**: Оптимизация структуры базы данных для конкретной СУБД, включая индексы, партиционирование и т.д.
5. **Реализация**: Создание базы данных и таблиц в СУБД.
#### Нормальные формы:
Нормальные формы помогают организовать данные в базе данных таким образом, чтобы избежать избыточности и обеспечить целостность данных.
1. **Первая нормальная форма (1NF)**:
   - Каждая таблица должна иметь уникальный первичный ключ.
   - Каждый столбец должен содержать атомарные значения (не должно быть массивов или списков в одном столбце).
2. **Вторая нормальная форма (2NF)**:
   - Таблица должна быть в 1NF.
   - Все неключевые атрибуты должны полностью зависеть от первичного ключа.
3. **Третья нормальная форма (3NF)**:
   - Таблица должна быть в 2NF.
   - Все атрибуты должны зависеть только от первичного ключа (не должно быть транзитивных зависимостей).
  
#### Индексы:
Индексы — это специальные структуры данных, которые ускоряют поиск и сортировку данных в базе данных. Они работают аналогично указателю в книге, который позволяет быстро найти нужную страницу без необходимости просматривать всю книгу.
- **Аналогия**: Представьте себе библиотеку с тысячами книг. Без каталога (индекса) вам придется просматривать каждую книгу, чтобы найти нужную. Каталог (индекс) позволяет быстро найти нужную книгу по автору, названию или теме.
- **Для чего нужны**:
  - **Ускорение поиска**: Индексы значительно ускоряют выполнение запросов, особенно в больших таблицах.
  - **Оптимизация сортировки**: Индексы помогают быстро сортировать данные по определенным столбцам.
  - **Уникальность данных**: Индексы могут обеспечивать уникальность значений в столбцах, что помогает избежать дублирования данных.
 
#### Пример создания базы данных:
```sql
-- Создание таблицы Category
CREATE TABLE category (
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор категории
    name VARCHAR(255) UNIQUE NOT NULL -- Уникальное имя категории
);
-- Создание таблицы Tag
CREATE TABLE tag (
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор тега
    name VARCHAR(255) UNIQUE NOT NULL -- Уникальное имя тега
);
-- Создание таблицы Article
CREATE TABLE article (
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор статьи
    title VARCHAR(255) NOT NULL, -- Заголовок статьи
    content TEXT NOT NULL, -- Содержание статьи
    publication_date TIMESTAMPTZ DEFAULT NOW(), -- Дата публикации статьи
    views INTEGER DEFAULT 0, -- Количество просмотров статьи
    category_id INTEGER NOT NULL DEFAULT 1, -- Идентификатор категории статьи
    slug VARCHAR(255) UNIQUE, -- Уникальный slug статьи
    is_active BOOLEAN DEFAULT TRUE, -- Статус активности статьи
    FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE -- Внешний ключ на таблицу Category
);
-- Создание таблицы для связи Article и Tag
CREATE TABLE article_tag (
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор связи
    article_id INTEGER NOT NULL, -- Идентификатор статьи
    tag_id INTEGER NOT NULL, -- Идентификатор тега
    FOREIGN KEY (article_id) REFERENCES article(id) ON DELETE CASCADE, -- Внешний ключ на таблицу Article
    FOREIGN KEY (tag_id) REFERENCES tag(id) ON DELETE CASCADE -- Внешний ключ на таблицу Tag
);
-- Создание индексов для ускорения поиска
CREATE INDEX idx_article_title ON article (title); -- Индекс для поиска по заголовку статьи
CREATE INDEX idx_article_slug ON article (slug); -- Индекс для поиска по slug статьи
-- Создание триггера для автоматического заполнения slug
CREATE OR REPLACE FUNCTION update_slug() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.slug IS NULL THEN
        NEW.slug := slugify(NEW.title); -- Функция slugify должна быть определена заранее
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER trigger_update_slug
BEFORE INSERT OR UPDATE ON article
FOR EACH ROW
EXECUTE FUNCTION update_slug();
```
**commit: `Урок 8: проектирование моделей баз данных: Оптимизация структуры базы данных для типичных задач`**

### Проектирование моделей баз данных: Оптимизация структуры базы данных для типичных задач
Проектирование базы данных — это процесс создания структуры базы данных, которая эффективно хранит, извлекает и управляет данными. Основные шаги проектирования базы данных включают:

#### Этапы проектирования базы данных:
1. **Сбор требований**: Определение, какие данные нужно хранить и как они будут использоваться.
2. **Концептуальное проектирование**: Создание ER-диаграмм (Entity-Relationship) для визуализации сущностей и их связей.
3. **Логическое проектирование**: Определение таблиц, столбцов, типов данных и ограничений.
4. **Физическое проектирование**: Оптимизация структуры базы данных для конкретной СУБД, включая индексы, партиционирование и т.д.
5. **Реализация**: Создание базы данных и таблиц в СУБД.

#### Нормальные формы:
Нормальные формы помогают организовать данные в базе данных таким образом, чтобы избежать избыточности и обеспечить целостность данных.
1. **Первая нормальная форма (1NF)**:
   - Каждая таблица должна иметь уникальный первичный ключ.
   - Каждый столбец должен содержать атомарные значения (не должно быть массивов или списков в одном столбце).
2. **Вторая нормальная форма (2NF)**:
   - Таблица должна быть в 1NF.
   - Все неключевые атрибуты должны полностью зависеть от первичного ключа.
3. **Третья нормальная форма (3NF)**:
   - Таблица должна быть в 2NF.
   - Все атрибуты должны зависеть только от первичного ключа (не должно быть транзитивных зависимостей).
  
#### Индексы:
Индексы — это специальные структуры данных, которые ускоряют поиск и сортировку данных в базе данных. Они работают аналогично указателю в книге, который позволяет быстро найти нужную страницу без необходимости просматривать всю книгу.
- **Аналогия**: Представьте себе библиотеку с тысячами книг. Без каталога (индекса) вам придется просматривать каждую книгу, чтобы найти нужную. Каталог (индекс) позволяет быстро найти нужную книгу по автору, названию или теме.
- **Для чего нужны**:
  - **Ускорение поиска**: Индексы значительно ускоряют выполнение запросов, особенно в больших таблицах.
  - **Оптимизация сортировки**: Индексы помогают быстро сортировать данные по определенным столбцам.
  - **Уникальность данных**: Индексы могут обеспечивать уникальность значений в столбцах, что помогает избежать дублирования данных.
 
#### Пример создания базы данных:
```sql
-- Создание таблицы Category
CREATE TABLE category (
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор категории
    name VARCHAR(255) UNIQUE NOT NULL -- Уникальное имя категории
);
-- Создание таблицы Tag
CREATE TABLE tag (
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор тега
    name VARCHAR(255) UNIQUE NOT NULL -- Уникальное имя тега
);
-- Создание таблицы Article
CREATE TABLE article (
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор статьи
    title VARCHAR(255) NOT NULL, -- Заголовок статьи
    content TEXT NOT NULL, -- Содержание статьи
    publication_date TIMESTAMPTZ DEFAULT NOW(), -- Дата публикации статьи
    views INTEGER DEFAULT 0, -- Количество просмотров статьи
    category_id INTEGER NOT NULL DEFAULT 1, -- Идентификатор категории статьи
    slug VARCHAR(255) UNIQUE, -- Уникальный slug статьи
    is_active BOOLEAN DEFAULT TRUE, -- Статус активности статьи
    FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE -- Внешний ключ на таблицу Category
);
-- Создание таблицы для связи Article и Tag
CREATE TABLE article_tag (
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор связи
    article_id INTEGER NOT NULL, -- Идентификатор статьи
    tag_id INTEGER NOT NULL, -- Идентификатор тега
    FOREIGN KEY (article_id) REFERENCES article(id) ON DELETE CASCADE, -- Внешний ключ на таблицу Article
    FOREIGN KEY (tag_id) REFERENCES tag(id) ON DELETE CASCADE -- Внешний ключ на таблицу Tag
);
-- Создание индексов для ускорения поиска
CREATE INDEX idx_article_title ON article (title); -- Индекс для поиска по заголовку статьи
CREATE INDEX idx_article_slug ON article (slug); -- Индекс для поиска по slug статьи
-- Создание триггера для автоматического заполнения slug
CREATE OR REPLACE FUNCTION update_slug() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.slug IS NULL THEN
        NEW.slug := slugify(NEW.title); -- Функция slugify должна быть определена заранее
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER trigger_update_slug
BEFORE INSERT OR UPDATE ON article
FOR EACH ROW
EXECUTE FUNCTION update_slug();
```
**commit: `Урок 8: проектирование моделей баз данных: Оптимизация структуры базы данных для типичных задач`**

### Решение практики с 8 урока
```python
# Задача 1: Найти все статьи, которые были опубликованы после 31 октября 2023 года.
# Фильтрация статей по дате публикации, которая больше 31 октября 2023 года.
articles = Article.objects.filter(publication_date__gt=timezone.datetime(2023, 10, 31))
print(articles)

# Задача 2: Найти все статьи, которые принадлежат категории "Образование" и имеют тег "Инновации".
# Создание объектов Q для условий фильтрации для категории "Образование" и тега "Инновации".
category_q = Q(category__name='Образование')
tag_q = Q(tags__name='Инновации')
# Комбинирование условий с использованием логического оператора AND.
articles = Article.objects.filter(category_q & tag_q)
print(articles)

# Задача 3: Найти все статьи, которые не принадлежат категории "Культура".
# Создание объекта Q для условия фильтрации для категории "Культура".
category_q = Q(category__name='Культура')
# Использование логического оператора NOT для инвертирования условия.
articles = Article.objects.filter(~category_q)
print(articles)

# Задача 4: Найти все статьи, которые принадлежат категории "Здоровье" или "Образование" и имеют тег "Исследования".
# Создание объектов Q для условий фильтрации для категорий "Здоровье" и "Образование" и тега "Исследования".
category_q1 = Q(category__name='Здоровье')
category_q2 = Q(category__name='Образование')
tag_q = Q(tags__name='Исследования')
# Комбинирование условий с использованием логических операторов OR и AND.
articles = Article.objects.filter((category_q1 | category_q2) & tag_q)
print(articles)

# Задача 5: Увеличить количество просмотров всех статей на 5.
# Использование класса F для создания выражения, которое ссылается на поле views.
# Обновление всех записей в таблице Article, увеличивая количество просмотров на 5.
Article.objects.update(views=F('views') + 5)

# Задача 6: Аннотировать все статьи с константным значением `is_featured` равным `False`.
# Использование метода annotate() для добавления нового поля is_featured со значением False ко всем статьям.
articles = Article.objects.annotate(is_featured=Value(False))
for article in articles:
    print(article.is_featured)  # Выведет False для всех статей
    
# Задача 7: Найти все статьи, которые были опубликованы в 2023 году.
# Фильтрация статей по году публикации, который равен 2023.
articles = Article.objects.filter(publication_date__year=2023)
print(articles)

# Задача 8: Найти все статьи, которые принадлежат категории "Технологии" и имеют тег "Инновации".
# Создание объектов Q для условий фильтрации для категории "Технологии" и тега "Инновации".
category_q = Q(category__name='Технологии')
tag_q = Q(tags__name='Инновации')
# Комбинирование условий с использованием логического оператора AND.
articles = Article.objects.filter(category_q & tag_q)
print(articles)

# Задача 9: Подсчитать количество статей в каждой категории.
# Использование метода values() для выбора поля category__name, по которому будем группировать данные.
# Использование метода annotate() для добавления нового поля count, которое представляет собой количество статей в каждой категории.
category_counts = Article.objects.values('category__name').annotate(count=Count('id'))
for category in category_counts:
    print(f"Category: {category['category__name']}, Count: {category['count']}")
    
# Задача 10: Подсчитать суммарное количество просмотров всех статей.
# Использование метода aggregate() для выполнения агрегатной операции суммирования над полем views.
total_views = Article.objects.aggregate(total_views=Sum('views'))
print(f"Total Views: {total_views['total_views']}")

# Задача 11: Найти статьи, у которых количество просмотров больше 150.
# Фильтрация статей по количеству просмотров, которое больше 150.
articles = Article.objects.filter(views__gt=150)
print(articles)

# Задача 12: Найти статьи, у которых количество просмотров меньше или равно 200.
# Фильтрация статей по количеству просмотров, которое меньше или равно 200.
articles = Article.objects.filter(views__lte=200)
print(articles)
```
**commit: `Урок 8: Решение практики с 7 урока`**