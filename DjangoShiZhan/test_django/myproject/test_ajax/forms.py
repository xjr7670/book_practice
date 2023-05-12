# -*- coding:utf-8 -*-
from django import forms


class PersonForm(forms.Form):
    id = forms.IntegerField(label='', widget=forms.widgets.NumberInput(attrs={'hidden': 'true'}), required=False)
    name = forms.CharField(
        label='Name',
        error_messages={
            'required': 'Cannot be void',
            'invalid': 'Format Error'
        },
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Please enter your name',
            'autofocus': True}
        )
    )
    email = forms.EmailField(
        label='Email',
        error_messages={
            'required': 'Cannot be empty',
            'invalid': 'Format Error'
        },
        widget=forms.widgets.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}
        )
    )
    salary = forms.DecimalField(
        label='Salary',
        error_messages={
            'required': 'Cannot be empty',
            'invalid': 'Format Error',
        },
        widget=forms.widgets.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Please enter your salary'}
        )
    )
