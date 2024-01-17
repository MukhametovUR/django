from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import  render_to_string
from django.views import View
from django.views.generic import TemplateView

from altrum.forms import AddPostForm, UploadedFileForm
from altrum.models import Altrum, Category, TagPost, UploadFiles

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

cats_db = [
    {'id': 1, 'name': 'Строительство'},
    {'id': 2, 'name': 'Доставка'},
    {'id': 3, 'name': 'Логистика'},

]


def index(request):
    posts = Altrum.published.all().select_related('cat')
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'altrum/index.html', context=data)


class WomenHome(TemplateView):
    template_name = 'altrum/index.html'
    extra_context = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': Altrum.published.all().select_related('cat'),
        'cat_selected': 0,
    }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Главная страница'
    #     context['menu'] = menu
    #     context['posts'] = Altrum.published.all().select_related('cat')
    #     context['cat_selected'] = int(self.request.GET.get('cat_id', 0))
    #     return context


def about(request):
    if request.method == 'POST':
        # handle_uploaded_file(request.FILES['file_upload'])
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadedFileForm()
    return render(request, 'altrum/about.html',
                  {'title': 'О сайте', 'menu': menu, 'form': form})


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
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    data = {
        'menu': menu,
        'title': 'Добавление статьи',
        'form': form
    }
    return render(request, 'altrum/addpage.html', data)


class AddPage(View):
    def get(self, request):
        form = AddPostForm()
        data = {
            'menu': menu,
            'title': 'Добавление статьи',
            'form': form
        }
        return render(request, 'altrum/addpage.html', data)


    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        data = {
            'menu': menu,
            'title': 'Добавление статьи',
            'form': form
        }
        return render(request, 'altrum/addpage.html', data)

def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_categories(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Altrum.published.filter(cat_id=category).select_related('cat')
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
    posts = tag.tags.filter(is_published=Altrum.Status.PUBLISHED).select_related('cat')
    data = {
        'title': f"Тег: {tag.tag}",
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'altrum/index.html', context=data)