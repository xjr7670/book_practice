#! -*- coding:utf-8 -*-
import traceback

from django.shortcuts import render, redirect, HttpResponse
from .models import Employee2, Department, Group, EmployeeInfo


def list_dep_old(request):
    dep_list = Department.objects.all()
    return render(request, 'test_orm_old/list_dep_old.html', {'dep_list': dep_list})


def add_dep_old(request):
    if request.method == 'POST':
        dep_name = request.POST.get('dep_name')
        dep_script = request.POST.get('dep_script')
        if dep_name.strip() == '':
            return render(request, 'test_orm_old/add_dep_old.html', {'error_info': '部门名称不能为空！'})
        try:
            p = Department.objects.create(dep_name=dep_name, dep_script=dep_script)
            return redirect('/test_orm_old/list_dep_old/')
        except Exception as e:
            traceback.print_exc(e)
            return render(request, 'test_orm_old/add_dep_old.html', {'error_info': '输入部门名称重复或信息有误！'})
        finally:
            pass

    return render(request, 'test_orm_old/add_dep_old.html')


def del_dep_old(request, dep_id):
    dep_object = Department.objects.get(id=dep_id)
    dep_object.delete()
    return redirect('/test_orm_old/list_dep_old')


def edit_dep_old(request, dep_id):
    if request.method == 'POST':
        id = request.POST.get('id')
        dep_name = request.POST.get('dep_name')
        dep_script = request.POST.get('dep_script')
        dep_object = Department.objects.get(id=id)

        dep_object.dep_name = dep_name
        dep_object.dep_script = dep_script

        dep_object.save()
        return redirect('/test_orm_old/list_dep_old/')
    else:
        dep_object = Department.objects.get(id=dep_id)
        print(dep_object.dep_name)
        return render(request, 'test_orm_old/edit_dep_old.html', {'department': dep_object})


def list_group_old(request):
    group_list = Group.objects.all()
    return render(request, 'test_orm_old/list_group_old.html', {'group_list': group_list})


def add_group_old(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        group_script = request.POST.get('group_script')
        if group_name.strip() == '':
            return render(request, 'test_orm_old/add_group.html', {'error_info': '团体名称不能为空'})
        try:
            Group.objects.create(group_name=group_name, group_script=group_script)
            return redirect('/test_orm_old/list_group_old')
        except Exception as e:
            return render(request, 'test_orm_old/add_group_old.html', {'error_info': '输入团体名称重复或信息有误'})
        finally:
            pass

    return render(request, 'test_orm_old/add_group_old.html')


def del_group_old(request, group_id):
    group_object = Group.objects.get(id=group_id)
    group_object.delete()
    return redirect('/test_orm_old/list_group_old/')


def edit_group_old(request, group_id):
    if request.method == 'POST':
        id = request.POST.get('id')
        group_name = request.POST.get('group_name')
        group_script = request.POST.get('group_script')
        group_object = Group.objects.get(id=id)
        group_object.group_name = group_name
        group_object.group_script = group_script
        group_object.save()
        return redirect('/test_orm_old/list_group_old')
    else:
        group_object = Group.objects.get(id=group_id)
        return render(request, 'test_orm_old/edit_group_old.html', {'group': group_object})


def list_employeeinfo_old(request):
    info_list = EmployeeInfo.objects.all()
    return render(request, 'test_orm_old/list_employeeinfo_old.html', {'info_list': info_list})


def add_employeeinfo_old(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        if phone.strip() == '':
            return render(request, 'test_orm_old/add_employeeinfo_old.html', {'error_info': '电话号码不能为空'})
        try:
            EmployeeInfo.objects.create(phone=phone, address=address)
            return redirect('/test_orm_old/list_employeeinfo_old/')
        except Exception as e:
            return render(request, 'test_orm_old/add_employeeinfo_old.html', {'error_info': '信息有误'})
        finally:
            pass

    return render(request, 'test_orm_old/add_employeeinfo_old.html')


def del_employeeinfo_old(request, info_id):
    info_object = EmployeeInfo.objects.get(id=info_id)
    info_object.delete()
    return redirect('/test_orm_old/list_employeeinfo_old/')


# edit the information of an employee
def edit_employeeinfo_old(request, info_id):
    if request.method == 'POST':
        id = request.POST.get('id')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        info_object = EmployeeInfo.objects.get(id=id)
        info_object.phone = phone
        info_object.address = address
        info_object.save()
        return redirect('/test_orm_old/list_employeeinfo_old/')
    else:
        info_object = EmployeeInfo.objects.get(id=info_id)
        return render(request, 'test_orm_old/edit_employeeinfo_old.html', {'info': info_object})


def list_employee_old(request):
    emp = Employee2.objects.all()
    return render(request, 'test_orm_old/list_employee_old.html', {'emp_list': emp})


def delete_employee_old(request, emp_id):
    emp = Employee2.objects.get(id=emp_id)
    emp.delete()
    return redirect('/test_orm_old/list_employee_old/')


def add_employee_old(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        dep = request.POST.get('dep')
        info = request.POST.get('info')
        salary = request.POST.get('salary')
        groups = request.POST.getlist('group')
        new_emp = Employee2.objects.create(name=name, email=email, salary=salary, dep_id=dep, info_id=info)
        new_emp.group.set(groups)
        return redirect('/test_orm_old/list_employee_old/')

    dep_list = Department.objects.all()
    group_list = Group.objects.all()
    info_list = EmployeeInfo.objects.all()
    return render(request,
                  'test_orm_old/add_employee_old.html',
                  {'dep_list': dep_list, 'group_list': group_list, 'info_list': info_list})


def edit_employee_old(request, emp_id):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        dep = request.POST.get('dep')
        info = request.POST.get('info')
        groups = request.POST.getlist('group')
        emp = Employee2.objects.get(id=id)
        emp.name = name
        emp.email = email
        emp.dep_id = dep
        emp.info_id = info
        emp.group.set(groups)
        emp.save()
        return redirect('/test_orm_old/list_employee_old/')

    emp = Employee2.objects.get(id=emp_id)
    dep_list = Department.objects.all()
    group_list = Group.objects.all()
    info_list = EmployeeInfo.objects.all()
    return render(request,
                  'test_orm_old/edit_employee_old.html',
                  {'emp': emp, 'dep_list': dep_list, 'info_list': info_list})


def test_foreign(request):
    emp = Employee2.objects.get(id=1)
    dep_name = emp.dep.dep_name
    dep_obj = Department.objects.get(id=1)
    emp_list = dep_obj.employee2_set.all()
    emp_names = [emp.name for emp in emp_list]

    return HttpResponse((f"1. 正向关联：员工名称：{emp.name}；所在部门名称：{dep_name}，<br>"
                         f"2. 反向查找：部门名称：{dep_obj.dep_name}；部门员工：{emp_names}"))

