from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

#from .forms import SiginForm
from .models import Sigup


@login_required
def home(request):
    return render(request, 'ui/home.html')


def login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            error = "Username and password are required and should not be empty"
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth(request, user)
                return redirect('home')
            else:
                error = "Wrong username or password"
    return render(request, 'ui/login.html', {'error': error})


def register(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not email or not phone_number or not password:
            error = "Username, email, phone number and password cannot be empty"
        else:
            user = Sigup(username=username, email=email, phone_number=phone_number)
            try:
                user.full_clean(exclude=['password'])
                validate_password(password, user)
                user.set_password(password)
                user.save()
            except ValidationError as e:
                error = ' '.join(e.messages)
            else:
                auth(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')

    return render(request, 'ui/register.html', {'error': error})
