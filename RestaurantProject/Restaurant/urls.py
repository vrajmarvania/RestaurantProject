from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('register',views.register,name='index'),
    path('registerform',views.registerform,name='index'),
    path('index',views.index,name='index'),
    path('logout',views.logout,name='index'),
    path('forgot-password',views.forgotp,name='index'),
    path('Restorent/<int:i>',views.Restorent,name='index'),
    path('loginc',views.loginc,name='index'),
    path('AddRestaurant',views.AddRestaurant,name='index'),
    path('AddFood',views.AddFood,name='index'),
    path('Order',views.Order,name='index'),
    path('NewOrder/<str:i>',views.NewOrder,name='index'),
    path('Norder/<str:i>',views.Norder,name='index'),
    path('DeleteF/<int:i>',views.DeleteF,name='index'),
    path('DeleteR/<int:i>',views.DeleteR,name='index'),
    path('UpdateF',views.UpdateF,name='index'),
    path('UpdateR',views.UpdateR,name='index'),
    path('RestorentDetails',views.RestorentDetails,name='index'),






]
