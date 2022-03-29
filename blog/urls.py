"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from app import views
from django.conf import settings ##新增
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('sort/', views.sort),
    path('login/', views.login),
    path('message/', views.message),
    path('about/', views.about),
    path('login/random_code/', views.get_random_code),
    path('sign/', views.sign),
    path('logout/', views.logout),
    path('backend/', views.backend), #后台个人中心
    path('backend/add_article/', views.add_article), #后台添加文章
    path('backend/edit_avatar/', views.edit_avatar), #后台修改头像
    path('backend/reset_password/', views.reset_password), #后台重置密码

    re_path(r'^backend/edit_article/(?P<nid>\d+)/', views.edit_article), #编辑文章
    re_path(r'^article/(?P<nid>\d+)/', views.article), #文章详情页
    re_path(r'^api/', include('api.urls')), #路由分发  将所有以api开头的请求分发到api这个urls.py中

    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),#用户上传文件路由配置
]
