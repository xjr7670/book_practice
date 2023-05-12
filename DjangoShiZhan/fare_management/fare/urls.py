# -*- coding:utf-8 -*-
from django.urls import path

from . import views


urlpatterns = [
    path('index/', views.index),
    path('carlist/', views.carlist),
    path('caradd/', views.caradd),
    path('caredit/<int:id>/', views.caredit),
    path('cardel/<int:id>/', views.cardel),
    path('deplist/', views.deplist),
    path('depadd/', views.depadd),
    path('depedit/<int:dep_id>/', views.depedit),
    path('depdel/<int:dep_id>/', views.depdel),
    path('userlist/', views.userlist),
    path('useredit/<int:user_id>/', views.useredit),
    path('farelist/', views.farelist),
    path('fareadd/', views.fareadd),
    path('fareedit/<int:fareid>/', views.fareedit),
    path('faredel/<int:fareid>/', views.faredel),
    path('farecheck/', views.farecheck),
    path('fareapprove/<str:ids>/', views.fare_approve),
    path('farecheck2/', views.farecheck2),
    path('approvecancel/', views.approve_cancel),
    path('annotate/', views.annotate_fare),
]
