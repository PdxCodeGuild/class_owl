from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    return render(request, 'users/login.html')

def signup(request):
    return render(request, 'users/signup.html')

def dashboard(request):
    return render(request, 'users/dashboard.html')

def logout(request):
    return redirect('users:login')