#!-*- coding:utf-8 -*-

import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from . import models, forms


def tangshi(request):
    return render(request, 'test_ajax/tangshi.html')


def tangshi_ret(request):
    ts1 = request.GET.get('ts1')
    ts2 = request.GET.get('ts2')
    dic = dict()
    if ts1 == '床前明月光':
        ts3 = '举头望明月'
        ts4 = '低头思故乡'
        dic = {
            'ts3': ts3,
            'ts4': ts4
        }

    data_set = json.dumps(dic)
    return HttpResponse(data_set)


def tangshi_img(request):
    src = "/media/default_header.jpg"
    return HttpResponse(src)


def list_person(request):
    per_list = models.Person.objects.all()
    return render(request, 'test_ajax/list_person.html', {'person_list': per_list})


def del_row(request):
    id = request.GET.get('id')
    models.Person.objects.filter(id=id).delete()
    return HttpResponse('Operation Success!')


def add_person(request):
    if request.method == 'POST':
        ret = {'status': 0, 'url_or_msg': ''}
        form_obj = forms.PersonForm(request.POST)

        if form_obj.is_valid():
            person_obj = models.Person.objects.create(
                name=form_obj.cleaned_data['name'],
                email=form_obj.cleaned_data['email'],
                salary=form_obj.cleaned_data['salary']
            )
            ret['url_or_msg'] = '/test_ajax/list_person/'
            return JsonResponse(ret)
        else:
            ret['status'] = 1
            ret['url_or_msg'] = form_obj.errors
            return JsonResponse(ret)
    form_obj = forms.PersonForm()

    return render(request, 'test_ajax/add_person.html', {'formobj': form_obj})


def test_name(request):
    ret = {'status': 0, 'message': ''}
    name = request.GET.get('name')
    per_obj = models.Person.objects.filter(name=name)

    if per_obj:
        ret['status'] = 1
        ret['message'] = 'Username already exists!'

    return JsonResponse(ret)

