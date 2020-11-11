from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def user_signup(request):
    if request.method=='POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        password = request.POST['password']
        email = request.POST['email']
        username = request.POST['username']
        security_question = request.POST['security_question']
        security_answer = request.POST['security_answer']
        
        user = User.objects.create_user(first_name=f_name,last_name=l_name,password=password,username=username,email=email,security_question=security_question,security_answer=security_answer)
        return redirect('users:login')
    elif request.method == 'GET':
        return render(request, 'users/index.html')

def user_login(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        
        if user is not None:

            login(request,user)

        return redirect('posts:index')
    elif request.method == 'GET':
        return render(request, 'users/login.html')



def user_logout(request):
    logout(request)
    return redirect('users:login')
