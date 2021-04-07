from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.User_login,name='login'),
    path('loginc', views.loginc, name='index'),
    path('index', views.Order, name='index'),
    path('NewOrder/<str:i>', views.NewOrder, name='index'),
    path('Norder/<str:i>', views.Norder, name='index'),
    path('User_login', views.User_login, name='index'),
    path('User_register', views.User_register, name='index'),
    path('User_registerform', views.User_registerform, name='index'),
    path('test', views.UData, name='index'),
    path('up', views.up, name='index'),
]
