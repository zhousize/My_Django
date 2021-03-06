"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
    项目的主路由配置文件，所有的动态路径必须先走该文件进行匹配
"""
from . import views
from django.contrib import admin
from django.urls import path,re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/1/',views.print_web1),    #增加一个http://127.0.0.1:8000/page/1/ 的对象地址
    path('page/2/',views.print_web2),    #增加一个http://127.0.0.1:8000/page/2/ 的对象地址
    path('str/<str:_str>', views.print_str),
    path('int/<int:_int>', views.print_int),
    path('slug/<slug:_slug>', views.print_slug),
    path('path/<path:_path>', views.print_path),
    path('test_poste', views.test_post),
    path('test',views.test_html),
    path('clac',views.my_clac),
    re_path(r'^(?P<x>\d{1,2})/(?P<y>\w{3})/(?P<z>\d{1,2})',views.print_algo),
]
'''
    path(route, views, name=None)
    参数：
    route: 字符串类型，匹配的请求路径
    views: 指定路径所对应的视图处理函数的名称
    name: 为地址起别名，在模板中地址反向解析时使用
'''

