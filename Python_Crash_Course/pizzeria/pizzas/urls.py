from django.conf.urls import url
from . import views

urlpatterns = [
        # 主页
        url(r'^$', views.index, name='index'),

        # 显示所有的pizza
        url(r"^pizzas/$", views.pizzas, name='pizzas'),

        # 显示特定pizza的页面
        url(r"^pizzas/(?P<pizza_id>\d+)/$", views.pizza, name='pizza'),
        ]
