from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Hoot, Comment

# Create your views here.
def index(request):

    hoots = Hoot.objects.order_by('-total_likes')[:5]

    context = {
        'hoots': hoots
    }

    return render(request, 'blog/index.html', context)

@login_required 
def create(request):

    request.method == "POST"
    form = request.POST
    title = form['title']
    body = form['body']
    image_url = form['image']
    published = form.get('publish', False)
    author = request.user

    if published:
        published = True
        date_published = timezone.now()
        hoot = Hoot(title=title, body=body, author=author, is_published=published, published_date=date_published, image=image_url)
    else:
        hoot = Hoot(title=title, body=body, author=author,
                    is_published=published, published_date=date_published, image=image_url)
    hoot.save()


    return render(request, 'blog/create.html')

def detail(request, blog_id):
    hoot = Hoot.objects.get(pk=blog_id)
    context = {
        'hoot': hoot
    }
    return render(request, 'blog/detail.html')

def delete_blog(request, blog_id):
    hoot = Hoot.objects.get(pk=blog_id)
    user = request.user
    if user == hoot.author:
        hoot.delete()

@login_required
def comment(request, blog_id):
    hoot = Hoot.objects.get(pk=blog_id)
    form= request.POST
    body = form['comment_body']
    comment = Comment(body, author=request.user, hoot=hoot)
    comment.save()

    return redirect('blog:detail', blog_id=blog_id)
