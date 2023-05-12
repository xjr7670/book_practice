# -*- coding:utf-8 -*-
from django import template
from django.db.models.aggregates import Count

from ..models import Blog, Category, Tag


register = template.Library()


@register.simple_tag
def get_new_blogs(num=5):
    return Blog.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Blog.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_blogs=Count('blog')).filter(num_blogs__gt=0)


@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_blogs=Count('blog')).filter(num_blogs__gt=0)

