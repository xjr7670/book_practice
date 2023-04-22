# -*- coding:utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError

from . import models


class RegForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        label='登录账号',
        error_messages={
            'max_length': '登录账号不能超过20位',
            'required': '登录账号不能为空',
        },
        widget=forms.widgets.TextInput(
            attrs={'class': 'form-control'},
        )
    )
    password = forms.CharField(
        min_length=6,
        label='密码',
        error_messages={
            'min_length': '密码最少为6位',
            'required': '密码不能为空',
        },
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'form-control'},
            render_value=True,
        )
    )
    repassword = forms.CharField(
        min_length=6,
        label='确认密码',
        error_messages={
            'min_length': '密码最少为6位',
            'required': '密码不能为空',
        },
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'form-control'},
            render_value=True,
        )
    )
    nickname = forms.CharField(
        max_length=20,
        required=False,
        label='姓名',
        error_messages={
            'max_length': '姓名不能超过20位',
        },
        initial='无名氏',
        widget=forms.widgets.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    email = forms.EmailField(
        label='邮箱',
        error_messages={
            'invalid': 'Wrong email address.',
            'required': 'Email must be fill',
        },
        widget=forms.widgets.EmailInput(
            attrs={'class': 'form-control'}
        )
    )
    telephone = forms.CharField(
        label='电话号码',
        required=False,
        error_messages={
            'max_length': 'No longer than 11',
        },
        widget=forms.widgets.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    head_img = forms.ImageField(
        label='头像',
        widget=forms.widgets.FileInput(
            attrs={'style': 'display: none'}
        )
    )

    def clean_username(self):
        uname = self.cleaned_data.get('username')
        vexist = models.Loguser.objects.filter(username=uname)
        if vexist:
            self.add_error('username', ValidationError('Account already exists!'))
        else:
            return uname

    def clean_repassword(self):
        passwd = self.cleaned_data.get('password')
        repasswd = self.cleaned_data.get('repassword')
        if repasswd and repasswd != passwd:
            self.add_error('repassword', ValidationError('Two password does not the same!'))
        else:
            return repasswd
