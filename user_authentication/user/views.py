from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # Log the user in and redirect to home page
            from django.contrib.auth import login
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("/login")
