from django.contrib import admin

# Register your models here.
from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews

#Региструруем мадели в админ.панели Django
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
