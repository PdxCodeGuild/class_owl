from django.shortcuts import render

# Create your views here.
def user_signup():
    return render(request, 'users/index.html')

def user_login():
    pass

def user_logout():
    pass