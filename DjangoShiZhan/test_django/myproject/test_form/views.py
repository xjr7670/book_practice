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


def add_loguser(request):
    if request.method == 'POST':
        form_obj = forms.LoguserForm(request.POST or None, request.FILES or None)
        if form_obj.is_valid():
            loguser_obj = models.LogUser.objects.create(
                account=form_obj.cleaned_data['account'],
                password=form_obj.cleaned_data['password'],
                email=form_obj.cleaned_data['email'],
                gender=form_obj.cleaned_data['gender'],
                hobby=form_obj.cleaned_data['hobby'],
                hair=form_obj.cleaned_data['hair'],
                img=form_obj.cleaned_data['img']
            )
            return redirect('/test_form/list_loguser/')
        else:
            return render(request, 'add_loguser.html', {'formobj': form_obj})

    form_obj = forms.LoguserForm()
    return render(request, 'add_loguser.html', {'formobj': form_obj})


def edit_loguser(request, loguser_id):
    if request.method == 'POST':
        form_obj = forms.LoguserForm(request.POST or None, request.FILES or None)
        if form_obj.is_valid():
            id = form_obj.cleaned_data['id']
            loguser_obj = models.LogUser.objects.get(id=id)
            loguser_obj.account = form_obj.cleaned_data['account']
            loguser_obj.password = form_obj.cleaned_data['password']
            loguser_obj.email = form_obj.cleaned_data['email']
            loguser_obj.gender = form_obj.cleaned_data['gender']
            loguser_obj.hobby = form_obj.cleaned_data['hobby']
            loguser_obj.hair = form_obj.cleaned_data['hair']
            loguser_obj.img = form_obj.cleaned_data['img']

            if not loguser_obj.img:
                loguser_obj.img = request.POST.get('img1')
            loguser_obj.save()
            imgname = loguser_obj.img
            return render(request, 'edit_loguser.html', {'formobj': form_obj, 'img': imgname})
        else:
            return render(request, 'add_loguser.html', {'formobj': form_obj})

    # when the request method is not POST
    obj_list = models.LogUser.objects.filter(id=loguser_id).values(
        'id', 'account', 'password', 'email', 'gender', 'hobby', 'hair', 'img'
    )
    dic = obj_list[0]
    imgname = dic['img']
    form_obj = forms.LoguserForm(initial=dic)
    return render(request, 'edit_loguser.html', {'formobj': form_obj, 'img': imgname})


def del_loguser(request, loguser_id):
    obj = models.LogUser.objects.get(id=loguser_id)
    obj.delete()
    return redirect('/test_form/list_loguser/')


def list_loguserm(request):
    users = models.LogUser.objects.all()
    return render(request, 'list_loguser1.html', {'usr_list': users})


def add_loguserm(request):
    if request.method == 'POST':
        form_obj = forms.LoguserModelForm(request.POST or None, request.FILES or None)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/test_form/list_loguserm/')
        else:
            return render(request, 'add_loguser1.html', {'formobj': form_obj})

    form_obj = forms.LoguserModelForm()
    return render(request, 'add_loguser1.html', {'formobj': form_obj})


def edit_loguserm(request, loguser_id):
    loguser_obj = models.LogUser.objects.get(id=loguser_id)
    if request.method == 'POST':
        form_obj = forms.LoguserModelForm(request.POST or None, request.FILES or None, instance=loguser_obj)
        if form_obj.is_valid():
            loguser = form_obj.save()
            imgname = loguser.img
            return render(request, 'edit_loguser1.html', {'formobj': form_obj, 'img': imgname})
        else:
            return render(request, 'add_loguser1.html', {'formobj': form_obj})

    imgname = loguser_obj.img
    form_obj = forms.LoguserModelForm(instance=loguser_obj)
    return render(request, 'edit_loguser1.html', {'formobj': form_obj, 'img': imgname})


def del_loguserm(request, loguser_id):
    obj = models.LogUser.objects.get(id=loguser_id)
    obj.delete()
    return redirect('/test_form/list_loguser/')

