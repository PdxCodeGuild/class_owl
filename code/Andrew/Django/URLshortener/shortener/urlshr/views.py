import random
import string
from django.conf.urls import url
from django.shortcuts import render, redirect
from .models          import ShortenedURL


# Create your views here.



def index(request):
    
    urls = ShortenedURL.objects.all()


    context = {
        'urls':urls
    }

    return render(request, 'urlshr/index.html', context)



def shorten(request):
    rand_string = ''
    options = list(string.ascii_letters + string.digits)
    
    for x in range(6):
        rand_string += random.choice(options)

    form = request.POST
    new_code = rand_string
    new_url = ShortenedURL(url = form['url'], code = new_code )

    new_url.save()

    return redirect('urlshr:index')


def go_to_site(request,id):
    
    site = ShortenedURL.objects.get(pk =id)

    site.visited += 1
    site.save()
    fsite = site.url

    fullsite = 'https://' + fsite

    
    return redirect(fullsite)