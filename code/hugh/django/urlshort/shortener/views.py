from django.http.response import JsonResponse
from django.shortcuts import render
import json
from string import hexdigits
import random
from . models import ShortenedURL

# Create your views here.
def index(request):
    #get list of URLS
    return render(request, 'shortener/index.html')

    #Render Index page

def get_urls(request):

    urls = ShortenedURL.objects.all()

    output = []
    for url in urls:
        output.append({
            'code': url.code,
            'url': url.url,
            'count': url.count
        })
    

    return JsonResponse({'urls':output})

# View 2 Form Submission
def post_urls(request):
    data = request.body

    data = json.loads(data) 

    long_url = data['URL']

    short_url = "".join([random.choice(hexdigits) for i in range (7)])

    shortened = ShortenedURL(code=short_url, url=long_url)

    shortened.save()

    print(data['URL'])
    return JsonResponse({'url':long_url,'code': short_url})