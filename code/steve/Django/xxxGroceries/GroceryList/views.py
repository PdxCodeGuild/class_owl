from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import GroceryList

# Create your views here.

def index(request):
    GroceryLists = GroceryList.objects.order_by()
    context = {
        'GroceryLists': GroceryList
    }
    return render(request, 'GroceryList/index.html', context)

def save_GroceryList(request):
    form = request.POST

    GroceryList = GroceryList(task=form['GroceryList_task'], priority=form['priority'])
    GroceryList.save()

    return HttpResponseRedirect(reverse('GroceryList:index'))

def toggle_complete(request, GroceryList_id):
    GroceryList = GroceryList.objects.get(pk= GroceryList_id)
    GroceryList.completed = not GroceryList.completed

    if GroceryList.completed:
        GroceryList.date_completed = timezone.now()

    GroceryList.save()
    return HttpResponseRedirect(reverse('GroceryList:index'))

def delete(request, GroceryList_id):
    GroceryList = GroceryList.objects.get(pk=GroceryList_id)
    GroceryList.delete()
    return HttpResponseRedirect(reverse('GroceryList:index'))