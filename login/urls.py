from os import name
from django.contrib import admin
from django.urls import path 
from django.urls import URLPattern
from . import views 

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('registerdisp',views.registerdisp,name="registerdisp"),
    path('logindisp',views.logindisp, name="logindisp"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    
    
]