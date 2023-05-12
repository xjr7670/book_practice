from django.shortcuts import render, redirect, HttpResponse
from django.conf import  settings

from rbac import models
from rbac.service.init_permission import init_permission


class BasePermPage(object):
    def __init__(self, code_list):
        self.code_list = code_list

    def has_add(self):
        if 'add' in self.code_list:
            return True

    def has_del(self):
        if 'del' in self.code_list:
            return True

    def has_edit(self):
        if 'edit' in self.code_list:
            return True


def login(request):
    if request.method == 'GET':
        return render(request, 'test_rbac/loign.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = models.UserInfo.objects.filter(username=username, password=password).first()
        if user:
            init_permission(request, user)
            return redirect('/index/')
        else:
            return render(request, 'test_rbac/login.html')


def logout(request):
    request.session.clear()
    return redirect('/login/')


def index(request):
    return render(request, 'test_rbac/index.html')


def userinfo(request):
    pagpermission = BasePermPage(request.session.get('permission_codes'))
    data_list = [
        {'id': 1, 'name': 'Zhang San', 'work': 'Lawyer'},
        {'id': 2, 'name': 'Li Si', 'work': 'Teacher'},
        {'id': 3, 'name': 'Wang Wu', 'work': 'Programmer'},
        {'id': 4, 'name': 'Zhao Liu', 'work': 'Doctor'},
        {'id': 5, 'name': 'Tian Qi', 'work': 'Nurse'},
    ]

    return render(request,
                  'test_rbac/userinfo.html',
                  {'data_list': data_list, 'pagpermission': pagpermission})


def userinfo_add(request):
    if request.method == 'GET':
        return render(request, 'test_rbac/useradd.html')
    else:
        return redirect('/userinfo/')


def userinfo_del(request, nid):
    return HttpResponse('Del user')


def userinfo_edit(request, nid):
    return HttpResponse('Edit user')


def department(request):
    pagpermission = BasePermPage(request.session.get('permission_codes'))
    return render(request, 'test_rbac/department.html', {'pagpermission': pagpermission})


def department_add(request):
    return HttpResponse('Add department')


def department_del(request):
    return HttpResponse('Delete department')


def department_edit(request):
    return HttpResponse('Edit department')


def order(request):
    pagpermission = BasePermPage(request.session.get('permission_codes'))
    return render(request, 'test_rbac/order.html', {'pagpermission': pagpermission})


def order_add(request):
    return HttpResponse('Add order')


def order_del(request):
    return HttpResponse('Delete order')


def order_edit(request):
    return HttpResponse('Edit order')
