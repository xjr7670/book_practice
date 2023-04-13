# -*- coding:utf-8 -*-
from django.urls import path
from test_form import views


urlpatterns = [
    path('login/', views.login),
    path('list_loguser/', views.list_loguser)
]