from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ShortenedURL

import random
from string import hexdigits

# Create your views here.

def index(request):
    short_urls = ShortenedURL.objects.order_by()

    context = {
        'short_urls': short_urls
    }
    return render(request, 'short/index.html', context)

def shortener(request):
    long_url = request.POST['long_url']
    # print(request.POST)
    if "https://" not in long_url:
        long_url = "https://" + long_url
    short_url = "".join([random.choice(hexdigits) for i in range(7)])
    shortened = ShortenedURL(code=short_url, url=long_url)
    shortened.save()
    print(shortened)
    return redirect('short:index')


def saver(request):
    pass


def redirector(request):
    pass

def shortlist(request):
    return render(request, 'short/shortlist.html')