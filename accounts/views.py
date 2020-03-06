from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
def register(request):
    if request.method == 'POST':
        #Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Check if passwords match
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
             if User.objects.filter(email=email).exists():
                messages.error(request, 'Email address is already registered')
                return redirect('register')
             else:
                 user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                 user.save()
                 messages.success(request, "You are registered now")
                 return redirect('login')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')