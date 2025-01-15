from django.contrib import admin  # (Not used here but might be for admin-related tasks elsewhere)
from django.urls import path, include  # Import functions to define URL patterns
from user import views  # Import the views module from the `user` app

urlpatterns = [
    # URL pattern for the home page
    path('', views.index, name="home"),
    
    # URL pattern for the login page
    path('login', views.login, name="login"),
    
    # URL pattern for the logout functionality
    path('logout', views.user_logout, name="logout"),
]
