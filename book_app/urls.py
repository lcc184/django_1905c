
from django.contrib import admin
from django.urls import path
from book_app import views
urlpatterns = [
    path('book/', views.login),#登陆功能的路由配置
    path('reg/', views.reg), # 注册功能的路由配置
]
