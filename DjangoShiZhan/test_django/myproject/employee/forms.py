# -*- coding:utf-8 -*-
from django import forms


class TestForm(forms.Form):
    account = forms.CharField(label='账号')
    password = forms.CharField(label='密码')
