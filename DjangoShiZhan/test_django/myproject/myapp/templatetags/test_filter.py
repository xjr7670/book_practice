# -*- coding:utf-8 -*-
from django import template

register = template.Library()


@register.filter(name='coderstatus')
def coder_status(value, arg):
    if value == 'morehair':
        return f'{arg} 是菜鸟程序员'
    if value == 'middlehair':
        return f'{arg} 是工程师级程序员'
    if value == 'fewhair':
        return f'{arg} 是资深程序员'

