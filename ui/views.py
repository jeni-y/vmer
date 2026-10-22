from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email  
from django.core.exceptions import ValidationError  

#from .forms import SiginForm
from .models import Sigup

@login_required
def home(request):
    return render(request, 'ui/home.html')

def login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        username = username.strip()
        password = password.strip()
        if not username or not password:
            error = "Username and password are required and should not be empty"

        else:
            user = authenticate(request, username = username, password = password)
            if user is not None:
                auth(request, user)
                return redirect('index')
            else:
                error = "Wrong username or password"
    return render(request, 'ui/login.html', {'error':error})

def register(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username','').strip()
        email = request.POST.get('email','').strip()
        phone_number = request.POST.get('phone_number','').strip()
        password = request.POST.get('password','').strip()

        if not username or not email or not phone_number or not password:
            error = "Username or email or phone_number or password cannot be empty"
        else:
            try:
                validate_email(email)

                if Sigup.objects.filter(username=username).exists():
                    error = "This username is already taken."
                elif Sigup.objects.filter(email=email).exists():
                    error = "This email is already registered."
                elif Sigup.objects.filter(phone_number=phone_number).exists():
                    error = "This phone number is already registered."
                
                else:
                    user = Sigup.objects.create_user(
                        username=username, email=email, 
                        phone_number=phone_number, password=password
                    )
                    user.save()
                    auth(request, user, backend='django.contrib.auth.backends.ModelBackend')
                
                    return redirect('index')
            except ValidationError:
                error = "Enter a valid email"


    return render(request, 'ui/register.html',{'error',error})


