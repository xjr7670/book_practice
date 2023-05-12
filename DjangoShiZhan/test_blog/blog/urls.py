# -*- coding:utf-8 -*-
from django.urls import path, re_path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('test_ckeditor_front/', views.test_ckeditor_front),
    path('', views.IndexView.as_view(), name='index'),
    path('registe/', views.registe, name='registe'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    re_path('blog/(?P<pk>[0-9]+)/', views.BlogDetailView.as_view(), name='detail'),
    re_path('category/(?P<pk>[0-9]+)/', views.CategoryView.as_view(), name='category'),
    re_path('tag/(?P<pk>[0-9]+)/', views.TagView.as_view(), name='tag'),
    re_path('archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/', views.archives, name='archives'),
    path('myindex/<int:loguserid>/', views.MyIndex.as_view(), name='myindex'),
    path('authorindex/<int:d>/', views.AuthorIndex.as_view(), name='authorindex'),

]
