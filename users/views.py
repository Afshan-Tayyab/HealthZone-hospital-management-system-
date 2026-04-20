from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib import messages
import resend
from django.conf import settings

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        
        if not username or not password:
            messages.error(request, "Username and password are required!")
            return render(request, 'signup.html')
        
        
        if User.objects.filter(username=username).exists():
            messages.error(request, f"Username '{username}' is already taken. Please choose another username.")
            return render(request, 'signup.html')
        
    
        if email and User.objects.filter(email=email).exists():
            messages.error(request, "Email address is already registered.")
            return render(request, 'signup.html')
        
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'signup.html')
        

        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters long.")
            return render(request, 'signup.html')
        
        try:
            
            user = User.objects.create_user(
                username=username,
                email=email if email else '',
                password=password
            )
            user.save()
            
            
            if email and hasattr(settings, 'RESEND_API_KEY') and settings.RESEND_API_KEY:
                try:
                    send_welcome_email(email, username)
                except Exception as e:
                    print(f"Email sending failed: {e}")
            
        
            auth_login(request, user)
            
            messages.success(request, f"Welcome {username}! Your account has been created successfully. 🏥")
            return redirect('/dashboard')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        
        if not username or not password:
            messages.error(request, "Please enter both username and password.")
            return render(request, 'login.html')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            
            auth_login(request, user)
            
            
            if not remember_me:
                request.session.set_expiry(0)  # Session expires when browser closes
            else:
                request.session.set_expiry(1209600)  # 2 weeks
            
            messages.success(request, f"Welcome back, {user.username}! 🏥")
            return redirect('/dashboard')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return render(request, 'login.html', {'username': username})
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully. 🏥")
    return redirect('/login')


def user_logout(request):
    logout(request)
    return redirect('/login')


def send_welcome_email(user_email, username):
    """Send welcome email to new user"""
    resend.api_key = settings.RESEND_API_KEY
    
    email_html = f'''
    <div style="font-family: Arial, sans-serif; max-width: 600px; background: #0c0004; color: #f8f5f6; padding: 30px; border-radius: 20px;">
        <h1 style="color: #ff4d6d;">Welcome {username}! 🏥</h1>
        <p>Thank you for joining <strong>HealthZone Hospital Management System</strong>.</p>
        <p>You can now:</p>
        <ul>
            <li>✓ Book appointments with doctors</li>
            <li>✓ View your medical history</li>
            <li>✓ Manage your health records</li>
        </ul>
        <p>Visit your dashboard: <a href="http://127.0.0.1:8000/dashboard/" style="color: #ff4d6d;">Click here</a></p>
        <br>
        <p>Best regards,<br><strong>HealthZone Team</strong></p>
    </div>
    '''
    
    resend.Emails.send(
        {
            'from': 'onboarding@resend.dev',
            'to': [user_email],
            'subject': 'Welcome to HealthZone HMS 🏥',
            'html': email_html
        }
    )