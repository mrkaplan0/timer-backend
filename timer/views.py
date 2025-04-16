from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import path
from . import views

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Validate passwords match
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'timer/pages/registration_page.html')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'timer/pages/registration_page.html')
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'timer/pages/registration_page.html')
        
        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        
        # Login the user
        login(request, user)
        
        # Redirect to dashboard
        return redirect('dashboard')
    
    return render(request, 'timer/pages/registration_page.html')

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'timer/pages/dashboard.html')

urlpatterns = [
    path('register/', views.register_view, name='register_page'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]