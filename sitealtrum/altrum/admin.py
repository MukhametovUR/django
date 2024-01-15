from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Altrum, Category


@admin.register(Altrum)
class AltrumAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'photo', 'post_photo', 'cat', 'tags']
    readonly_fields = ['post_photo']
    prepopulated_fields = {'slug': ('title',)}
    # filter_horizontal = ['tags']
    filter_vertical = ['tags']
    # exclude = ['tags', 'is_published']
    list_display = ('title', 'post_photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('title',)
    ordering = ['-time_create', 'title']
    list_editable = ('is_published',)
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']
    list_filter = ['cat__name', 'is_published']
    save_on_top = True

    @admin.display(description="Изображение", ordering='content')
    def post_photo(self, altrum: Altrum):
        if altrum.photo:
            return mark_safe(f"'<img src='{altrum.photo.url}' width=50>")
        else:
            return "Без фото"

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Altrum.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей")

    @admin.action(description='Снять с публикации')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Altrum.Status.DRAFT)
        self.message_user(request, f"{count} записей снято с публикации!", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

