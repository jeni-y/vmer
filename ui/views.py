from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .form import VmForm

import json
import os
import subprocess
import tempfile

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
                return redirect('index')
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


def home(request):
    return render(request, 'home.html')

@login_required
def index(request):
    return render(request,'index.html',{'username':request.user.username})

@login_required
def vm(request):
    error = None
    if request.method == "POST":
        form = VmForm(request.POST)
        if form.is_valid():
           
            vm_instance = form.save(commit=False)
            vm_instance.username = request.user
            vm_instance.save()

          
            json_data = {
                "vm_name": vm_instance.vm_name,
                "ssh_key": vm_instance.ssh_key,
                "user": request.user.username,
            }

            with tempfile.NamedTemporaryFile(
                mode="w", delete=False, suffix=".json"
            ) as temp_file:
                json.dump(json_data, temp_file, indent=4)
                temp_file_path = temp_file.name  

            try:
                binary_path = "/absolute/path/to/your/vmpro"  
                command = [binary_path, temp_file_path]

               
                result = subprocess.run(
                    command, capture_output=True, text=True, check=True
                )


                print("C Code Output:", result.stdout)

            except subprocess.CalledProcessError as e:
               
                error = f"Execution failed: {e.stderr}"
                print("C Code Error:", e.stderr)

            finally:

                if os.path.exists(temp_file_path):
                    os.remove(temp_file_path)

            if not error:
                return redirect("index")  
        else:
            error = "Invalid form submission. Check your fields."
    else:
        form = VmForm()

    return render(request, "vm.html", {"form": form, "error": error})



def later(request):
    return render(request,'later.html')
