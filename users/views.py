from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        print("DEBUG - Username:", username)
        print("DEBUG - Email:", email)
        print("DEBUG - Password:", password)
        
        if not username or not password:
            messages.error(request, "Username and password are required!")
            return render(request, 'signup.html')
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'signup.html')
        
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters!")
            return render(request, 'signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return render(request, 'signup.html')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        auth_login(request, user)
        messages.success(request, f"Welcome {username}!")
        return redirect('/dashboard/')
    
    return render(request, 'signup.html')