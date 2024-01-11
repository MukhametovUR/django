from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator

from altrum.models import Category


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=5,
                            label="Заголовок",
                            widget=forms.TextInput(attrs={'class': 'form-input'}),
                            error_messages={
                                'min-length': 'Слишком короткий заголовок',
                                'required': 'Без заголовка никак'
                            })
    slug = forms.SlugField(max_length=255, label="URL",
                           validators=[
                               MinLengthValidator(5),
                               MaxLengthValidator(100)
                           ])
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows':5}), required=False, label="Контент")
    is_published = forms.BooleanField(required=False, label="Статус", initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label="Категории",empty_label="Категория не выбрана")


    def clean_title(self):
        title = self.cleaned_data['title']
        ALLOWED_CHARS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя123456789- '

        if not (set(title) <= set(ALLOWED_CHARS)):
            raise ValidationError('Должны присутствовать только русские символы, дефис и пробел')
