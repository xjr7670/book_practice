# -*- coding:utf-8 -*-
from django.urls import path, re_path

from . import views


urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name='index'),
    path('userinfo/', views.userinfo, name='userinfo_list'),
    path('userinfo_add/', views.userinfo_add, name='userinfo_add'),
    re_path('userinfo/edit/(\\d+)/', views.userinfo_edit, name='userinfo_edit'),
    path('userinfo/del(\\d+)/', views.userinfo_del, name='userinfo_del'),
    path('department/', views.department, name='department_list'),
    path('department/add/', views.department_add, name='department_add'),
    path('department/edit/(\\d+)/', views.department_edit, name='department_edit'),
    path('department/del/(\\d+)/', views.department_del, name='department_del'),

]