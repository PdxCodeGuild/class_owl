from django.shortcuts import render, reverse
from django.http import HttpResponse
from .models import GroceryList
from django.http import HttpResponseRedirect
from django.utils import timezone

# Create your views here.
def index(request):
    list_items = GroceryList.objects.order_by('description')
    context = {
        'list_items': list_items
    }
    return render(request, 'grocerylist/index.html', context)

def save_list_item(request):
    form = request.POST

    list_item = GroceryList(description=form['grocery_list_item'],created_date=timezone.now())
    
    list_item.save()
    return HttpResponseRedirect(reverse('grocerylist:index'))


def toggle_complete(request, list_item_id):
    list_item = GroceryList.objects.get(pk= list_item_id)
    list_item.completed = not list_item.completed

    if list_item.completed:
        list_item.completed_date = timezone.now()

    list_item.save()
    return HttpResponseRedirect(reverse('grocerylist:index'))


def delete(request, list_item_id):
    list_item = GroceryList.objects.get(pk=list_item_id)
    list_item.delete()
    return HttpResponseRedirect(reverse('grocerylist:index'))