import datetime
import json

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponse

from . import models
from rbac import models as rbac_models


def login(request):
    if request.method == 'GET':
        return render(request, 'fare/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = rbac_models.UserInfo.objects.filter(username=username, password=password).first()
        if user:
            request.session['user_nickname'] = user.nickname
            request.session['user_dep'] = user.loguser.dep_id
            return redirect('/fare/index/')
        else:
            return render(request, 'fare/login.html')


def logout(request):
    request.session.clear()
    rep = redirect('/login/')
    rep.cookies.clear()
    return rep


def index(request):
    return render(request, 'index.html')


def carlist(request):
    carlist = models.CarInfo.objects.all()
    return render(request, 'fare/carinfo_list.html', {'carlist': carlist})


def caradd(request):
    if request.method == 'POST':
        plate_number = request.POST.get('plate_number')
        driver = request.POST.get('driver')
        price = request.POST.get('price')
        remarks = request.POST.get('remarks')
        models.CarInfo.objects.create(plate_number=plate_number,
                                      driver=driver,
                                      price=price,
                                      remarks=remarks)
        return redirect('/fare/carlist/')
    return render(request, 'fare/carinfo_add.html')


def caredit(request, id):
    if request.method == 'POST':
        obj_id = request.POST.get('id')
        car_obj = models.CarInfo.objects.get(id=obj_id)
        plate_number = request.POST.get('plate_number')
        driver = request.POST.get('driver')
        price = request.POST.get('price')
        remarks = request.POST.get('remarks')

        car_obj.plate_number = plate_number
        car_obj.driver = driver
        car_obj.price = price
        car_obj.remarks = remarks
        car_obj.save()

        return redirect('/fare/carlist/')
    car_obj = models.CarInfo.objects.get(id=id)
    return render(request, 'fare/carinfo_edit.html', {'obj': car_obj})


def cardel(request, id):
    car_obj = models.CarInfo.objects.get(id=id)
    car_obj.delete()
    return redirect('/fare/carlist/')


def deplist(request):
    dep_list = models.Department.objects.all()
    return render(request, 'fare/dep_list.html', {'deplist': dep_list})


def depadd(request):
    if request.method == 'POST':
        dep_name = request.POST.get('dep_name')
        dep_script = request.POST.get('dep_script')
        models.Department.objects.create(dep_name=dep_name, dep_script=dep_script)
        return redirect('/fare/deplist/')
    return render(request, 'fare/dep_add.html')


def depedit(request, dep_id):
    if request.method == 'POST':
        obj_id = request.POST.get('id')
        dep_name = request.POST.get('dep_name')
        dep_script = request.POST.get('dep_script')
        models.Department.objects.filter(id=obj_id).update(dep_name=dep_name, dep_script=dep_script)
        return redirect('/fare/deplist/')
    dep_obj = models.Department.objects.get(id=dep_id)
    return render(request, 'fare/dep_edit.html', {'obj': dep_obj})


def depdel(request, dep_id):
    dep_obj = models.Department.objects.get(id=dep_id)
    dep_obj.delete()
    return redirect('/fare/deplist/')


def userlist(request):
    user_list = rbac_models.UserInfo.objects.all()
    return render(request, 'fare/userinfo_list.html', {'user_list': user_list})


def useredit(request, user_id):
    if request.method == 'POST':
        _id = request.POST.get('id')
        user_obj = rbac_models.UserInfo.objects.get(id=_id)
        dep_id = request.POST.get('dep_id')
        try:
            loguser_id = user_obj.loguser.id
            models.LogUser.objects.filter(id=loguser_id).update(dep_id=dep_id)
        except ObjectDoesNotExist:
            models.LogUser.objects.create(dep_id=dep_id, user_obj_id=_id)
        return redirect('/fare/userlist/')
    user_obj = rbac_models.UserInfo.objects.get(id=user_id)
    dep_list = models.Department.objects.all()
    return render(request, 'fare/userinfo_edit.html', {'obj': user_obj, 'deplist': dep_list})


def farelist(request):
    tday = datetime.datetime.now().date()
    cur_dep = request.session.get('user_dep')
    fare_list = models.Fare.objects.all().filter(drive_date=tday, dep_id=cur_dep, approve_status='0')
    fare_list = models.Fare.objects.all()
    return render(request, 'fare/fare_list.html', {'fare_list': fare_list})


def faredel(request, fareid):
    ret = {'status': False}
    try:
        obj = models.Fare.objects.get(id=fareid)
        obj.delete()
        ret['status'] = True
    except Exception:
        ret['status'] = False

    return HttpResponse(json.dumps(ret))


def fareadd(request):
    tday = datetime.datetime.now().strftime('%Y-%m-%d')
    cur_dep = request.session.get('user_dep')
    dep_obj = models.Department.objects.get(id=3)
    car_list = models.CarInfo.objects.all()
    user_nickname = request.session.get('user_nickname')
    if request.method == 'POST':
        passenger = request.POST.get('passenger')
        carid = request.POST.get('car_id')
        driver = request.POST.get('driver')
        price = request.POST.get('price')
        distance = request.POST.get('distance')
        fare = request.POST.get('fare')
        remark = request.POST.get('remark')
        drive_date = datetime.datetime.now().date()
        models.Fare.objects.create(dep_id=dep_obj.id,
                                   passenger=passenger,
                                   car_id=carid,
                                   driver=driver,
                                   price=price,
                                   distance=distance,
                                   fare=fare,
                                   drive_date=drive_date,
                                   remark=remark,
                                   operator='Lisa',
                                   approve_status='0')
        return redirect('/fare/farelist/')
    return render(request,
                  'fare/fare_add.html',
                  {'dep_obj': dep_obj, 'carlist': car_list, 'tday': tday, 'nickname': 'Lisa'})


def fareedit(request, fareid):
    tday = datetime.datetime.now().strftime('%Y-%m-%d')
    cur_dep = request.session.get('user_dep')
    dep_obj = models.Department.objects.get(id=3)
    car_list = models.CarInfo.objects.all()
    user_nickname = request.session.get('user_nickname')

    if request.method == 'POST':
        fareid = request.POST.get('id')
        cur_dep = request.POST.get('dep_id')
        passenger = request.POST.get('passenger')
        carid = request.POST.get('car_id')
        driver = request.POST.get('driver')
        price = request.POST.get('price')
        distance = request.POST.get('distance')
        fare = request.POST.get('fare')
        remark = request.POST.get('remark')
        drive_date = request.POST.get('drive_date')
        models.Fare.objects.filter(id=fareid).update(dep_id=cur_dep,
                                                     passenger=passenger,
                                                     car_id=carid,
                                                     driver=driver,
                                                     price=price,
                                                     distance=distance,
                                                     fare=fare,
                                                     drive_date=drive_date,
                                                     remark=remark,
                                                     operator='Lisa')
        return redirect('/fare/farelist/')
    fare_obj = models.Fare.objects.get(id=fareid)
    car_list = models.CarInfo.objects.all()
    return render(request, 'fare/fare_edit.html', {'obj': fare_obj, 'carlist': car_list})

