import datetime
import json

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Sum

from . import models
from rbac import models as rbac_models
from rbac.service.init_permission import init_permission
from utils.paginater import Paginater


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
        return render(request, 'fare/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = rbac_models.UserInfo.objects.filter(username=username, password=password).first()
        if user:
            init_permission(request, user)
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
    pagpermission = BasePermPage(request.session.get('permission_codes'))
    carlist = models.CarInfo.objects.all()
    return render(request, 'fare/carinfo_list.html', {'carlist': carlist, 'pagpermission': pagpermission})


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


def farecheck(request):
    dep_list = models.Department.objects.all()
    if request.method == 'POST':
        dep_id = request.POST.get('department', None)
        drive_date1 = request.POST.get('drive_date1', None)
        drive_date2 = request.POST.get('drive_date2', None)
        conditions_dic = {'approve_status': '0'}
        if dep_id:
            conditions_dic['dep_id'] = int(dep_id)
        if drive_date1:
            conditions_dic['drive_date__gte'] = drive_date1
        if drive_date2:
            conditions_dic['drive_date__lte'] = drive_date2
        if conditions_dic:
            total_count = models.Fare.objects.filter(**conditions_dic).count()
        else:
            total_count = models.Fare.objects.all().count()

        cur_page_num = request.GET.get('page')
        if not cur_page_num:
            cur_page_num = '1'

        one_page_lines = 10
        page_maxtag = 7
        page_obj = Paginater(url_address='/fare/farecheck/',
                             cur_page_num=cur_page_num,
                             total_rows=total_count,
                             one_page_lines=one_page_lines,
                             page_maxtag=page_maxtag)
        if conditions_dic:
            fare_list = models.Fare.objects.filter(**conditions_dic).order_by('drive_date')[page_obj.data_start:page_obj.data_end]
        else:
            fare_list = models.Fare.objects.all().order_by('drive_date')[page_obj.data_start:page_obj.data_end]
        return render(request,
                      'fare/farelist_check.html',
                      {'fare_list': fare_list,
                       'page_nav': page_obj.html_page(),
                       'dep_list': dep_list,
                       'conditins': conditions_dic})

    cur_page_num = request.GET.get('page')
    if not cur_page_num:
        cur_page_num = '1'
    total_count = models.Fare.objects.filter(approve_status='0').count()
    one_page_lines = 10
    page_maxtag = 7
    page_obj = Paginater(url_address='/fare/farecheck/',
                         cur_page_num=cur_page_num,
                         total_rows=total_count,
                         one_page_lines=one_page_lines,
                         page_maxtag=page_maxtag)
    fare_list = models.Fare.objects.filter(approve_status='0').order_by('drive_date')[page_obj.data_start:page_obj.data_end]
    return render(request,
                  'fare/farelist_check.html',
                  {'fare_list': fare_list,
                   'page_nav': page_obj.html_page(),
                   'dep_list': dep_list})


def fare_approve(request, ids):
    vids = ids.split(',')
    int_ids = []
    for i in vids:
        ii = int(i)
        int_ids.append(ii)
    ret = {'status': False}
    try:
        models.Fare.objects.filter(id__in=vids).update(approve_status='1')
        ret['status'] = True
    except Exception:
        ret['status'] = False
    return HttpResponse(json.dumps(ret))


def farecheck2(request):
    dep_list = models.Department.objects.all()
    if request.method == 'POST':
        dep_id = request.POST.get('department', None)
        drive_date1 = request.POST.get('drive_date1', None)
        drive_date2 = request.POST.get('drive_date2', None)
        conditions_dic = {'approve_status': '1'}

        if dep_id:
            conditions_dic['dep_id'] = int(dep_id)
        if drive_date1:
            conditions_dic['drive_date__gte'] = drive_date1
        if drive_date2:
            conditions_dic['drive_date__lte'] = drive_date2
        if conditions_dic:
            total_count = models.Fare.objects.filter(**conditions_dic).count()
        else:
            total_count = models.Fare.objects.all().count()
        cur_page_num = request.GEt.get('page')
        if not cur_page_num:
            cur_page_num = '1'
        one_page_lines = 10
        page_maxtag = 7
        page_obj = Paginater(url_address='/fare/farecheck2/',
                             cur_page_num=cur_page_num,
                             total_rows=total_count,
                             one_page_lines=one_page_lines,
                             page_maxtag=page_maxtag)
        if conditions_dic:
            fare_list = models.Fare.objects.filter(**conditions_dic).order_by('drive_date')[page_obj.data_start:page_obj.data_end]
        else:
            fare_list = models.Fare.objects.all().order_by('drive_date')[page_obj.data_start: page_obj.data_end]
        return render(request,
                      'fare/farelist_check2.html',
                      {'fare_list': fare_list,
                       'page_nav': page_obj.html_page(),
                       'dep_list': dep_list,
                       'conditions': conditions_dic})


def approve_cancel(request, ids):
    vids = ids.split(',')
    int_ids = []
    for i in vids:
        ii = int(i)
        int_ids.append(ii)
    ret = {'status': False}
    try:
        models.Fare.objects.filter(id__in=vids).update(approve_status='0')
        ret['status'] = True
    except Exception:
        ret['status'] = False
    return HttpResponse(json.dumps(ret))


def annotate_fare(request):
    farelist = models.Fare.objects.values('dep__dep_name',
                                          'drive_date__year',
                                          'drive_date__month',
                                          'approve_status').annotate(sum_distance=Sum('distance'),
                                                                     sum_fare=Sum('fare')).values('dep__dep_name',
                                                                                                  'drive_date__year',
                                                                                                  'drive_date__month',
                                                                                                  'approve_status',
                                                                                                  'sum_distance',
                                                                                                  'sum_fare')
    faredic = {}
    begin = True
    depname = ''
    distance0_xj = 0
    fare0_xj = 0
    distance1_xj = 0
    fare1_xj = 0
    distance_xj = 0
    fare_xj = 0
    distance0_hj = 0
    fare0_hj = 0
    distance1_hj = 0
    fare1_hj = 0
    distance_hj = 0
    fare_hj = 0

    for fare in farelist:
        if begin:
            begin = False
            depname = fare['dep__dep_name']
        if depname != fare['dep__dep_name']:
            onefare = {'dep__dep_name': '小计',
                       'sum_distance0': distance0_xj,
                       'sum_fare0': fare0_xj,
                       'sum_distance1': distance1_xj,
                       'sum_fare1': fare1_xj,
                       'sum_distance': distance_xj,
                       'sum_fare': fare_xj}
            faredic[depname+'xj'] = onefare
            distance_xj = 0
            fare0_xj = 0
            distance1_xj = 0
            fare1_xj = 0
            distance_xj = 0
            fare_xj = 0
            depname = fare['dep__dep_name']
        distance_xj += fare['sum_distance']
        fare_xj += fare['sum_fare']
        distance_hj += fare['sum_distance']
        fare_hj += fare['sum_fare']
        if fare['approve_status'] == '0':
            distance0_xj += fare['sum_distance']
            fare0_xj += fare['sum_fare']
            distance0_hj += fare['sum_distance']
            fare0_hj += fare['sum_fare']
        if fare['approve_status'] == '1':
            distance1_xj += fare['sum_distance']
            fare1_xj += fare['sum_fare']
            distance1_hj += fare['sum_distance']
            fare1_hj += fare['sum_fare']

        vid = fare['dep__dep_name'] + str(fare['drive_date__year']) + str(fare['drive_date__month'])
        if vid in faredic:
            if fare['approve_status'] == '0':
                faredic[vid]['sum_distance0'] = fare['sum_distance']
                faredic[vid]['sum_fare0'] = fare['sum_fare']
            if fare['approve_status'] == '1':
                faredic[vid]['sum_distance1'] = fare['sum_distance']
                faredic[vid]['sum_fare1'] = fare['sum_fare']

            if 'sum_distance0' in faredic[vid]:
                distance0 = faredic[vid]['sum_distance0']
                fare0 = faredic[vid]['sum_fare0']
            else:
                distance0 = 0
                fare0 = 0

            if 'sum_distance1' in faredic[vid]:
                distance1 = faredic[vid]['sum_distance1']
                fare1 = faredic[vid]['sum_fare1']
            else:
                distance1 = 0
                fare1 = 0

            faredic[vid]['sum_distance'] = distance0 + distance1
            faredic[vid]['sum_fare'] = fare0 + fare1
        else:
            onefare = {
                'dep__dep_name': fare['dep__dep_name'],
                'drive_date__year': fare['drive_date__year'],
                'drive_date__month': fare['drive_date__month'],
            }
            if fare['approve_status'] == '0':
                onefare['sum_distance0'] = fare['sum_distance']
                onefare['sum_fare0'] = fare['sum_fare']
            if fare['approve_status'] == '1':
                onefare['sum_distance1'] = fare['sum_distance']
                onefare['sum_fare1'] = fare['sum_fare']
            faredic[vid] = onefare
            if 'sum_distance0' in onefare:
                distance0 = onefare['sum_distance0']
                fare0 = onefare['sum_fare0']
            else:
                distance0 = 0
                fare0 = 0

            if 'sum_distance1' in onefare:
                distance1 = onefare['sum_distance1']
                fare1 = onefare['sum_fare1']
            else:
                distance1 = 0
                fare1 = 0

            onefare['sum_distance'] = distance0 + distance1
            onefare['sum_fare'] = fare0 + fare1
            faredic[vid] = onefare

    onefare = {'dep__dep_name': '小计',
               'sum_distance0': distance0_xj,
               'sum_fare0': fare0_xj,
               'sum_distance1': distance1_xj,
               'sum_fare1': fare1_xj,
               'sum_distance': distance_xj,
               'sum_fare': fare_xj}
    faredic[depname + 'xj'] = onefare

    onefare = {
        'dep__dep_name': '合计',
        'sum_distance0': distance0_hj,
        'sum_fare0': fare0_hj,
        'sum_distance1': distance1_hj,
        'sum_fare1': fare1_hj,
        'sum_distance': distance_hj,
        'sum_fare': fare_hj,
    }

    faredic[depname + 'hj'] = onefare

    return render(request, 'fare/fare_addup.html', {'faredic': faredic})




