from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path('',views.index, name="home"),
    path('login',views.login, name="login"),
    path('logout',views.user_logout, name="logout"),
]