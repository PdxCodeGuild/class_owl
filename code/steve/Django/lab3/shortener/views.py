from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ShortenedURL

import json
import random
from string import hexdigits



# View 1 returns a page for entering in a url to be shortened, and a list of urls that have been shortened 
def index(request):
    # Get list of urls

    # Render index page
    return render(request, 'shortener/index.html')

def get_urls(request):
    urls = ShortenedURL.objects.all()
    output = []
    for url in urls:
        output.append({
            'code': url.code,
            'url': url.url,
            'count': url.count
        })

    return JsonResponse({'urls': output})

def post_urls(request):
    data = request.body
    data = json.loads(data)
    print(data['URL'])
    long_url = data['URL']
    if "https://" not in long_url:
        long_url = "https://" + long_url

    short_url = "".join([random.choice(hexdigits) for i in range(7)])
    shortened = ShortenedURL(code=short_url, url=long_url)
    shortened.save()
    return JsonResponse({'url': long_url, 'code': short_url})

def go_to_urls(request, code):
    url = ShortenedURL.objects.get(code=code)

    url.count +=1
    url.save()

    return redirect(url.url)

# View 2 for receiving the form submission containing the long url, generating a random string, 
# and saving it to the database (localhost:8000/shortener/save/)
# View 3 performs the redirecting, which takes a code as a parameter (localhost:8000/shortener/pEc4vt/). 
# Be sure to include the protocol ("https://") in the urls or redirecting will not work properly.


