"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from myapp import views
from . import settings
from test_form import views as form_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('test_orm_old/', include('employee.urls')),
    path('myapp/', include('myapp.urls')),
    path('test_view/', include('test_view.urls')),
    path('hello/', views.hello),
    path('ny/<int:year>/<int:month>/', views.ny, name='ny'),
    path('name/<str:username>/', views.name, name='name'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('test_orm/', include('employee.urls')),
    path('test_form/', include('test_form.urls')),
    path('test_page/', include('test_page.urls')),
    path('test_ajax/', include('test_ajax.urls')),
    path('test_middleware/', include('test_middleware.urls')),
    path('test_auth/', include('test_auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
