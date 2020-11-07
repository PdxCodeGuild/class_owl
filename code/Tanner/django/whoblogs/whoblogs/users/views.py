from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blogs.models import Hoot, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginuser(request):
    error = None
    if request.method == "POST":
        form = request.POST
        username = form['username']
        password = form['password']

        user = authenticate(request, username=username, password=password)
        if user == None:
            error = "incorrect"
        else:
            login(request, user)
            return redirect('users:dashboard')
    return render(request, 'users/login.html')

def signup(request):
    error = None
    if request.method == "POST":
        form = request.POST
        firstname = form['firstname']
        lastname = form['lastname']
        username = form['username']
        email = form['email']
        password = form['password']
        password2 = form['password2']

        if User.objects.filter(username=username).exists():
            error = "username already exists"
        elif User.objects.filter(email=email).exists():
            error = "email already exists"
        elif password != password2:
            error = "Passwords do not match"
        else:
            user = User.objects.create_user(username=username, first_name= firstname, last_name = lastname, email=email, password=password)
            user.save()
            return redirect('users:dashboard')
    
    return render(request, 'users/signup.html', {'error': error})
    

def dashboard(request):
    hoot = Hoot.objects.filter_by(author=request.user).order_by('created_date')
    context = {
        'hoot': hoot
    }
    return render(request, 'users/dashboard.html', context)

@login_required
def logoutuser(request):
    logout(request)
    return redirect('blog:index')


