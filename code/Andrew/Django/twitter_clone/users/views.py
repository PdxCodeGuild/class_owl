from django.shortcuts import redirect, render
from .models import CreateUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def create_user(request):

    form = request.POST
    username = form['username']
    password = form['password']
    email = form['email']
    
    print(username, password, email)
    full_user = User.objects.create_user(username = username, password=password, email=email)

    print(full_user.password)
    return redirect('users:log_in')


def index(request):


    return render(request, 'users/index.html')

def log_in(request):
    
    if request.POST:
        
        form = request.POST
        username= form['username']
        password= form['password']

        user = authenticate(request, username = username, password = password)


        if user:
            login(request, user)
            return redirect('posts:index')

        else:
            message = 'Invalid Log In Attempt'
            context = {
                'message': message
            }

            return render(request, 'users/log_in.html', context)

    return render(request, 'users/log_in.html')

def log_out(request):
    
    logout(request)

    return redirect('posts:index')
