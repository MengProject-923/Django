from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users, name='get_users'),

    ## 添加相应的接口名称
    path('migrations/', views.get_migrations, name='get_migrations'),

    path('update_users/', views.update_users, name='update_users'),
]
