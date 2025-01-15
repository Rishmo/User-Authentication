from django.shortcuts import render, redirect  # Import functions to render templates and redirect users
from django.contrib.auth.models import User  # Import the User model for user-related operations
from django.contrib.auth import logout, authenticate  # Import functions for authentication and logout

# Create your views here.

def index(request):
    # Check if the user is not authenticated (anonymous)
    if request.user.is_anonymous:
        return redirect("/login")  # Redirect anonymous users to the login page
    return render(request, "index.html")  # Render the index.html template for authenticated users

def login(request):
    if request.method == "POST":  # Handle POST requests for login
        username = request.POST.get('username')  # Get the username from the POST data
        password = request.POST.get('password')  # Get the password from the POST data
        
        # Authenticate the user against the database
        user = authenticate(username=username, password=password)
        if user is not None:  # If authentication is successful
            from django.contrib.auth import login  # Import login function dynamically
            login(request, user)  # Log the user in
            return redirect("/")  # Redirect the user to the homepage
        else:
            # If authentication fails, render the login page with an error message
            return render(request, "login.html", {"error": "Invalid credentials"})

    # Render the login page for GET requests
    return render(request, "login.html")

def user_logout(request):
    logout(request)  # Log the user out and clear the session
    return redirect("/login")  # Redirect to the login page
