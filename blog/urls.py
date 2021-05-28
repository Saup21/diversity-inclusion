from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/create/', views.new_post, name='new_post'),
    path('post/detail/<int:pk>/',views.detailpost, name='detail'),
    path('path/detail/<int:pk>/comment/',views.comm,name="comment"),
]
