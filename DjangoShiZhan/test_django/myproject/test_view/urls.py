# -*- coding:utf-8 -*-
from django.conf import settings
from django.urls import path
from django.views.static import serve

from . import views

urlpatterns = [
    path('hello_view/', views.hello_view),
    path('dep/<int:dep_id>/', views.depdetail, name='depdetail'),
    path('test_redirect/', views.test_redirect),
    path('test_templateview/', views.TestTemplateview.as_view()),
    path('listviewdemo/', views.ListviewDemo.as_view()),
    path('detailviewdemo/<int:personid>/', views.DetailviewDemo.as_view()),
    path('login/', views.login),
    path('index/', views.index),
    path('add_person/', views.add_person),
    path('del_person/<int:personid>/', views.del_person),
    path('edit_person/<int:personid>/', views.edit_person),

]
