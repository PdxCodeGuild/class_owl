from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.
def index(request):

    blog_posts = BlogPost.objects.order_by('-likes')

    context = {
        'message': 'apple bottom jeans',
        'blog_posts': blog_posts
    }
    return render(request, 'kmpf/index.html', context)

def about(request):
    context = {
        'message': 'hi'
    }  

    return render(request, 'kmpf/about.html', context)
    