from django.shortcuts import render, redirect, HttpResponse
from . import forms
from . import models


def login(request):
    if request.method == 'POST':
        form_obj = forms.LoginForm(request.POST)
        if form_obj.is_valid():
            account = form_obj.cleaned_data['account']
            pwd = form_obj.cleaned_data['pwd']
            user_obj = models.LogUser.objects.filter(account=account, password=pwd).first()
            if user_obj:
                return redirect('/list_loguser/')
            else:
                error = '用户不存在或密码错误'
                return render(request, 'login.html', {'form_obj': form_obj, 'errmsg': error})
        else:
            return render(request, 'login.html', {'form_obj': form_obj})

    form_obj = forms.LoginForm()
    return render(request, 'test_orm/login.html', {'form_obj': form_obj})


def list_loguser(request):
    users = models.LogUser.objects.all()
    return render(request, 'list_loguser.html', {'usr_list': users})

