from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect


def user_login(request):
    if request.method == 'GET':
        return render(request, 'test_auth/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = authenticate(username=username, password=password)
        if user_obj:
            login(request, user_obj)
            return redirect('/test_auth/index/')
        else:
            return render(request, 'test_auth/login.html')


def logout(request):
    request.session.clear()
    return redirect('/test_auth/user_login/')


def index(request):
    return render(request, 'test_auth/index.html')


def userinfo(request):
    data_list = [
        {'id': 1, 'name': 'Zhang San', 'work': 'Lawyer'},
        {'id': 2, 'name': 'Li Si', 'work': 'Teacher'},
        {'id': 3, 'name': 'Wang Wu', 'work': 'Programmer'},
        {'id': 4, 'name': 'Zhao Liu', 'work': 'Doctor'},
        {'id': 5, 'name': 'Tian Qi', 'work': 'Nurse'},
    ]

    return render(request, 'test_auth/userinfo.html', {'data_list': data_list})


def userinfo_add(request):
    if request.method == 'GET':
        return render(request, 'test_auth/useradd.html')
    else:
        return redirect('/test_auth/userinfo/')


def userinfo_del(request, nid):
    return HttpResponse('Delete user')


def userinfo_edit(request, nid):
    return HttpResponse('Edit user')


def department(request):
    return render(request, 'test_auth/department.html')


def department_add(request):
    return HttpResponse('Add department')


def department_del(request):
    return HttpResponse('Delete department')


def department_edit(request):
    return HttpResponse('Edit department')
