from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from.models import Hught
# Create your views here.

#@login_required
def index(request):
    hught = Hught.objects.all
    context = {
        'hught': hught
    }
    return render(request, 'hught/index.html', context)

#@login_required
def save_hught(request):
    form = request.POST

   
    hught = Hught(title=form['title'], body=form['body'])
    hught.save()

    return HttpResponseRedirect(reverse('hught:index'))

@login_required
def delete_hught(request, hught_id):
    hught = Hught.objects.get(pk=hught_id)
    hught.delete_hught()
    return HttpResponseRedirect(reverse('hught:index'))