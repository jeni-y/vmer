from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    username = request.user.username
    return render(request, 'home.html', {'username': username})

# Create your views here.
def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')


def login_verify(request):
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
                auth_login(request, user)
                return redirect('home')
            else:
                error = "Wrong username or password"
    return render(request, 'login.html', {'error':error})



def register_user(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        if not username or not email or not password:
            error = "All fields are required."
        else:
            try:
                validate_email(email)

                if User.objects.filter(username=username).exists():
                    error = "Username already exists."
                elif User.objects.filter(email=email).exists():
                    error = "Email already exists."
                else:
                    User.objects.create_user(
                        username=username,
                        email=email,
                        password=password
                    )
                    return render(
                        request,
                        'login.html',
                        {'message': 'Registration successful! Please log in.'}
                    )

            except ValidationError:
                error = "Enter a valid email address."

    return render(request, 'register.html', {'error': error})

@login_required
def home(request):
    return render(request, 'home.html')