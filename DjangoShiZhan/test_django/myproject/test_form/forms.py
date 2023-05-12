# -*- coding:utf-8 -*-
from django import forms
from . import models


class LoginForm(forms.Form):
    account = forms.CharField(
        min_length=2,
        label='账号',
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control", "placeholder": "Please input your account", "accountfocus": True}
        )
    )

    pwd = forms.CharField(
        min_length=6,
        label='密码',
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'form-control', "placeholder": "please Enter your password"}, render_value=True
        ),
    )


class LoguserForm(forms.Form):
    id = forms.IntegerField(label='', widget=forms.widgets.NumberInput(attrs={'hidden': 'true'}), required=False)
    account = forms.CharField(
        label='账号',
        widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter account', 'autofocus': True})
    )
    password = forms.CharField(
        label='密码',
        widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter password'})
    )
    email = forms.EmailField(
        label='邮箱',
        widget=forms.widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter email'})
    )
    gender = forms.ChoiceField(
        choices=((1, '男'), (2, '女')),
        label='性别',
        initial='1',
        widget=forms.widgets.RadioSelect()
    )
    hobby = forms.ChoiceField(
        choices=((1, '游泳'), (2, '自行车'), (3, '跑酷')),
        label='爱好',
        initial=3,
        widget=forms.widgets.Select()
    )
    hair = forms.ChoiceField(
        label='发量',
        choices=((1, '很多'), (2, '一般'), (3, '很少')),
        widget=forms.widgets.RadioSelect()
    )
    img = forms.ImageField(label='头像', required=False)


class LoguserModelForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=((1, '男'), (2, '女')),
        label='性别',
        initial='1',
        widget=forms.widgets.RadioSelect()
    )
    hobby = forms.ChoiceField(
        choices=((1, '游泳'), (2, '自行车'), (3, '跑酷')),
        label='爱好',
        initial=3,
        widget=forms.widgets.Select()
    )
    hair = forms.ChoiceField(
        label='发量',
        choices=((1, '很多'), (2, '一般'), (3, '很少')),
        widget=forms.widgets.RadioSelect()
    )

    class Meta:
        model = models.LogUser
        fields = '__all__'
        labels = {
            'account': '账号',
            'password': '密码',
            'email': '邮箱',
            'img': '头像'
        }
        widgets = {
            'account': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter account', 'autofocus': True}),
            'password': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter password'}),
            'email': forms.widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter email'})
        }
