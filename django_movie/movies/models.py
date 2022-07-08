from django.db import models
from datetime from date

# Create your models here.
#импорт Models из django.db
class Category(models.Model):
    #Описание полей - экземпляры классов полей
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    #Возвращает строковое представление модели
    def __str__(self):
        return self.name

    #Контейнер класса с некоторыми опциями
    #Прикрепленные к модели
    class Meta:
        verbose_name = "Категория"
        verbose_name_plurar = "Категория"

#Модель для режиссеров и актеров
class Actor(models.Model):
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/")

    # Возвращает строковое представление модели
    def __str__(self):
        return self.name

    # Контейнер класса с некоторыми опциями
    # Прикрепленные к модели
    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plurar = "Актеры и режиссеры"

class Genre(models.Model):
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField(max_length=160, unique=True)

    # Возвращает строковое представление модели
    def __str__(self):
        return self.name

    # Контейнер класса с некоторыми опциями
    # Прикрепленные к модели
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plurar = "Жанр"

class Movie(models.Model):
    name = models.CharField("Название", max_length=100)
    tagLine = models.TextField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2022)
    country = models.CharField("Страна", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    actors = models.ManyToManyField("Жанры", verbose_name="жанры")
    world_premiere = models.DateField("Премьеры в мире", default=date.today)
    bunget = models.PositiveSmallIntegerField("Бюджет", default=0, help_text="указывать сумму в долларах")
    fess_in_usa = models.PositiveIntegerField(
        "Сборы в США", default=0, help_text="указывать сумму в долларах"
    )
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    # Возвращает строковое представление модели
    def __str__(self):
        return self.name

    # Контейнер класса с некоторыми опциями
    # Прикрепленные к модели
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plurar = "Фильм"