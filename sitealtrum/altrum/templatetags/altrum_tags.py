from django import template
import altrum.views as views
from altrum.models import Category, TagPost

register = template.Library()


@register.inclusion_tag('altrum/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('altrum/list_tags.html')
def show_all_tags():
    cats = Category.objects.all()
    return {'tags': TagPost.objects.all()}