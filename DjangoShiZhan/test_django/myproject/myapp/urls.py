# -*- coding:utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('test/', views.test),
    path('login/', views.login),
    path('template_test/', views.template_test),
    path('test_filter/', views.test_filter),
    path('test_for/', views.test_for),
    path('test_tag/', views.test_tag),
    path('test_inclusiontag/', views.test_inclusion_tag),
    path('test_motherboard/', views.mother_test),
]
