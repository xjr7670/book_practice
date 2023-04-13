# -*- coding:utf-8 -*-
from django import forms


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
