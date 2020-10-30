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
    if request.method == "POST":
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
            Hoot(title=title, body=body, author=author, is_published=published, image=image_url)
        hoot.save()
        return redirect('users:dashboard')

    return render(request, 'blog/create.html')

def detail(request, blog_id):
    pass

def delete_blog(request, blog_id):
    pass
