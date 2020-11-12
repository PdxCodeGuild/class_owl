from pathlib import PosixPath
from typing import ContextManager
from django.http import request
from django.shortcuts import render, redirect
from .models import Chirp
from django.contrib.auth.decorators import login_required

# Create your views here.
# post_chirp

def index(request):

    chirps = Chirp.objects.all

    context = {
        'chirps': chirps,
    }

    return render(request,'posts/index.html',context)

def save_chirp(request):

   form = request.POST
   chirp = Chirp(message=form['message'], user=request.user)
   chirp.save()

   return redirect('posts:index')