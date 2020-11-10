from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Chirp
from django.utils import timezone


# Create your views here.

def index(request):
    
    chirps = Chirp.objects.order_by('-created_at')[0:6]

    user = request.user
    context = {
        'chirps': chirps,
        'user': user
    }

    return render(request, 'posts/index.html', context)

@login_required
def dashboard(request):
    user = request.user
    chirps = Chirp.objects.filter(user=user)

    context = {
        'chirps': chirps
    }

    return render(request, 'posts/dashboard.html', context)


@login_required
def create_post(request):
    form = request.POST
    user = request.user
    message = form['message']

    if len(message) > 250:
        return redirect('posts:dashboard')

    new_chirp = Chirp(user = user, message = message, created_at = timezone.now())

    new_chirp.save()

    return redirect('posts:dashboard')

def public_dash(request, chirp_id):
    """
    docstring
    """
    chirp_author = Chirp.objects.get(pk = chirp_id).user
    chirps = Chirp.objects.filter(user=chirp_author)
    
    if request.user.is_authenticated:
        if request.user == chirp_author: 
            return redirect('posts:dashboard')
    
    context ={
        'chirps': chirps,
        'author': chirp_author
    }
    return render(request, 'posts/public_dash.html', context)



def likes(request, num):
    
    chirp = Chirp.objects.get(pk = num)
    
    mood = request.GET['mood']
    
    
    if mood == 'like':
        chirp.likes += 1
        chirp.save()
        
    elif mood =='dislike':
        chirp.likes -= 1
        chirp.save()
        

    return redirect('posts:index')

@login_required
def delete_post(request, chirp_id):
    chirp = Chirp.objects.get(pk = chirp_id)

    chirp.delete()

    return redirect('posts:dashboard')







