# -*- coding:utf-8 -*-
from django import template


register = template.Library()


@register.simple_tag(name='test_simpletag')
def test_simpletag(arg1, arg2, arg3):
    return f'这是一个 simpletag 示例，它接收的参数分别是：{arg1}、{arg2}、{arg3}'


@register.inclusion_tag('inclusion_tag_html.html')
def test_inclusiontag(name):
    name1 = f"{name}'s experience: "
    data = ['Primary programmer, Just familiar', 'Advance programmer, Skillful', 'Ultimate Programmer, Profession']
    return {'name': name1, 'data': data}

