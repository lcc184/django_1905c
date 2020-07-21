
from django.contrib import admin
from django.urls import path
from book_app import views
urlpatterns = [
    path('book/', views.login),
]
