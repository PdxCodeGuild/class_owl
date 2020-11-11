from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from.models import Grocery
# Create your views here.

def index(request):
    grocerys = Grocery.objects.order_by('-gnumber')
    context = {
        'grocerys': grocerys
    }
    return render(request, 'grocery/index.html', context)

def save_grocery(request):
    form = request.POST
    
    grocery = Grocery(grocery_task=form['grocery_task'], due_date=form['due_date'], recipe=form['recipe'], )
    grocery.save()

    return HttpResponseRedirect(reverse('grocery:index'))

#toggles completed status by taking in the grocery ID from the page, and flipping the completed status in the DB
def toggle_complete(request, grocery_id):
    # pk means primary key, but you can call it what you want
    grocery = Grocery.objects.get(pk= grocery_id)
    grocery.completed = not grocery.completed

    if grocery.completed:
        grocery.date_completed = timezone.now()

    grocery.save()
    return HttpResponseRedirect(reverse('grocery:index'))

def delete(request, grocery_id):
    grocery = Grocery.objects.get(pk=grocery_id)
    grocery.delete()
    return HttpResponseRedirect(reverse('grocery:index'))