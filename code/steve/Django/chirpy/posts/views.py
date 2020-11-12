from typing import ContextManager
from django.http import request
from django.shortcuts import render
from .models import Chirp

# Create your views here.
# post_chirp

def index(request):

    chirps = Chirp.objects.all

    context = {
        'chirps': chirps,
    }

    return render(request,'posts/index.html',context)

def save_chirp(request):

    chirp = Chirp(body)

    context = {

    }