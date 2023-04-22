# -*- coding:utf-8 -*-
from django.urls import path
from test_form import views


urlpatterns = [
    path('login/', views.login),
    path('list_loguser/', views.list_loguser),
    path('add_loguser/', views.add_loguser),
    path('edit_loguser/<int:loguser_id>/', views.edit_loguser),
    path('del_loguser/<int:loguser_id>/', views.del_loguser),
    path('list_loguserm/', views.list_loguserm),
    path('del_loguserm/<int:loguser_id>/', views.del_loguserm),
    path('add_loguserm/', views.add_loguserm),
    path('edit_loguserm/<int:loguser_id>/', views.edit_loguserm),
]