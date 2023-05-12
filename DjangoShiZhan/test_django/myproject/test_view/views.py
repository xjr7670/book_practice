#! -*- coding:utf-8 -*-

import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, ListView, DetailView
from . import models


def hello_view(request):
    vnow = datetime.datetime.now().date()
    rep = "<div align='center'><h1>你好，欢迎光临本页面</h1><hr>当前日期是：%s</div>" % vnow
    return HttpResponse(rep)


def depdetail(request, dep_id):
    obj = models.Department.objects.get(id=dep_id)
    return HttpResponse('部门：' + obj.dep_name + ', 备注：' + obj.dep_script)


def test_redirect(request):
    obj = models.Department.objects.get(id=1)
    return redirect(obj)


class TestTemplateview(TemplateView):
    template_name = 'test_view/test_temp.html'

    def get_context_data(self, **kwargs):
        context = super(TestTemplateview, self).get_context_data(**kwargs)
        context['test'] = '这是一个要传递的变量'
        return context


class ListviewDemo(ListView):
    model = models.Department
    template_name = 'test_view/listviewdemo.html'
    context_object_name = 'person_list'

    def get_queryset(self):
        personlist = models.Person.objects.filter(gender='1')
        return personlist

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['loguser'] = models.LogUser.objects.all().first()
        return super(ListviewDemo, self).get_context_data(**kwargs)


class DetailviewDemo(DetailView):
    model = models.Person
    template_name = 'test_view/testdetail.html'
    context_object_name = 'person'
    pk_url_kwarg = 'personid'

    def get_object(self, queryset=None):
        obj = super(DetailviewDemo, self).get_object()
        if obj.gender == '1':
            obj.gender = '男'
        else:
            obj.gender = '女'
        return obj

    def get_context_data(self, **kwargs):
        kwargs['test'] = '这是一个 DetailView 类通用视图生成的页面'
        return super(DetailviewDemo, self).get_context_data(**kwargs)


def login(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        loguser = models.LogUser.objects.filter(account=account, password=password).first()
        if loguser:
            rep = redirect('/test_view/index/')
            if remember == 'on':
                rep.set_cookie('account', account, max_age=60*60*8)
            return rep
        else:
            errmsg = '用户名或密码错误！'
            return render(request, 'test_view/login.html', {'errmsg': errmsg})

    account = request.COOKIES.get('account', '')
    return render(request, 'test_view/login.html', {'account_two': account})


def index(request):
    person_list = models.Person.objects.all()
    return render(request, 'test_view/index.html', {'person_list': person_list})


def add_person(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        head_img = request.FILES.get('head_img')
        attachment = request.FILES.get('attachment')
        new_person = models.Person.objects.create(
                        name=name,
                        email=email,
                        gender=gender,
                        head_img=head_img,
                        attachment=attachment
                    )
        return redirect('/test_view/index/')
    return render(request, 'test_view/add_person.html')


def edit_person(request, personid):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        head_img = request.FILES.get('head_img')
        attachment = request.FILES.get('attachment')
        person = models.Person.objects.get(id=id)
        person.name = name
        person.email = email
        person.gender = gender
        if head_img:
            person.head_img = head_img
        if attachment:
            person.attachment = attachment
        person.save()
        return redirect('/test_view/index/')
    person_obj = models.Person.objects.get(id=personid)
    return render(request, 'test_view/edit_person.html', {'person': person_obj})


def del_person(request, personid):
    person_obj = models.Person.objects.get(id=personid)
    person_obj.delete()
    return redirect('/test_view/index/')
