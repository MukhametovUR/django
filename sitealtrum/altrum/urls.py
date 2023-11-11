from django.urls import path, re_path, register_converter
from . import views
from . import converters
register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'), #http://127.0.0.1:8000/
    path('cats/<int:cat_id>/', views.categories, name='cats_id'), #http://127.0.0.1:8000/categories/
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),  # http://127.0.0.1:8000/categories/
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive)
    path("archive/<year4:year>/", views.archive, name='archive')
]