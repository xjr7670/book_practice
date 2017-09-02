"""定义blogs的URL模式"""

from django.conf.urls import url
from . import views

urlpatterns = [
        # 主页
        url(r'^$', views.index, name='index'),

        # 添加博文的表单
        url(r'^new_blog/$', views.new_blog, name="new_blog"),

        # 修改博文的表单
        url(r'^edit_post/(?P<post_id>\d+)/$', views.edit_post, name="edit_post"),
        ]
