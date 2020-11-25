from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from void.models import Conversation, Comment

# Create your views here.
def loginUser(request):
    error = None
    if request.method == "POST":
        form = request.POST
        username = form['username']
        password = form['password']

        user = authenticate(request, username=username, password=password)
        if user == None:
            error = "Username or password is incorrect"
        else:
            login(request, user)
            return redirect('users:dashboard')

    return render(request, 'users/login.html', {'error': error})

def signUp(request):
    error = None
    if request.method == "Post":
        form = request.Post
        firstname = form['firstname']
        lastname = form['lastname']
        username = form['username']
        email = form['email']
        password = form['password']
        password2 = form['password']

        if User.object.filter(username=username).exists():
            error = "This User Name is already taken"
        elif User.objects.filter(email=email).exists():
            error = "This Email is already in user"
        elif password2 != password:
            error = "Passwords do not match"
        else:
            user = User.objects.create_user(
                username=username, first_name=firstname, last_name=lastname, email=email, password=password)
            user.save()
            return redirect('users:login')

    return render(request, 'users/signup.html', {'error': error})

@login_required
def dashboard(request):

    conversations = Conversation.objects.filter(
        author=request.user).order_by('created_date')

    context = {
        'conversations': conversations
    }
    return render(request, 'users/dashboard.html', context)

@login_required 
def logoutUser(request):
    logout(request)
    return redirect('void:index')
 
