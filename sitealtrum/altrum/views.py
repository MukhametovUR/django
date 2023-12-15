from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import  render_to_string

from altrum.models import Altrum, Category, TagPost

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]
data_db = [
    {'id': 1, 'title': 'Строительство под ключ', 'content': 'Строительство под ключ', 'is_published': True},
    {'id': 2, 'title': 'Доставка материалов', 'content': 'Доставка до пункта назначения', 'is_published': False},
    {'id': 3, 'title': 'Строительство и логистика', 'content': 'Полный цикл логистики и строительства', 'is_published': True}
]

cats_db = [
    {'id': 1, 'name': 'Строительство'},
    {'id': 2, 'name': 'Доставка'},
    {'id': 3, 'name': 'Логистика'},

]
def index(request):
    posts = Altrum.published.all()
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'altrum/index.html', context=data)

def about(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': data_db,
            }
    return render(request, 'altrum/index.html', data)


def about(request):
    return render(request, 'altrum/about.html', {'title': 'О сайте', 'menu': menu})


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        uri = reverse('home')
        return redirect(uri)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def show_post(request, post_slug):
    post = get_object_or_404(Altrum, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1
    }
    return render(request, 'altrum/post.html', data)


def add_page(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_categories(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Altrum.published.filter(cat_id=category)
    data = {
        'title': f'Главная страница: {category.name}',
        'menu': menu,
        'posts': data_db,
        'cat_selected': category.pk,
    }
    return render(request, 'altrum/index.html', context=data)


def page_not_found(request):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Altrum.Status.PUBLISHED)
    data = {
        'title': f"Тег: {tag.tag}",
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'altrum/index.html', context=data)