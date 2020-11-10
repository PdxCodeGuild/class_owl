from django.shortcuts import redirect, render
from django.urls import reverse
from .models import CreateUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def create_user(request):
    error = ''
    taken = ''
    form = request.POST
    username = form.get('username')
    password = form.get('password')
    email = form.get('email')

    if username == None:
        return render(request, 'users/index.html', {'error': 'Invalid Setup!'})

    elif len(username)> 50 or len(password)>23 or password =='' or username == '':
        return render(request, 'users/index.html', {'error': 'Invalid Setup!'})

    is_taken = User.objects.get(username =username)
    if is_taken == None:

        full_user = User.objects.create_user(username = username, password=password, email=email)
        return redirect('users:log_in')

    return render(request, 'users/index.html', {'taken': 'Username is taken'})




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
