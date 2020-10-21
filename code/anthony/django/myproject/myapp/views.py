from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.


def index(request):

    blog_posts = BlogPost.objects.order_by('-likes')

    context = {
        'message': 'Apple Bottom Jeans',
        'blog_posts': blog_posts
    }
    return render(request, 'myapp/index.html', context)


def about(request):

    context = {
        'message': 'Boots With the Fur'
    }

    return render(request, 'myapp/about.html')
