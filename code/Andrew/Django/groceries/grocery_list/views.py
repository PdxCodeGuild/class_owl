from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, reverse
from django.utils import timezone
from .models import Grocery_item
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):

    grocery_items = Grocery_item.objects.order_by('description')

    context ={
        'grocery_items': grocery_items
    }

    return render(request, 'grocery_list/index.html', context)


def add_item(request):
    form = request.POST
    
    grocery_item = Grocery_item(description = form['g_item'])

    print(grocery_item)
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))



def completed_item(request, id):
    form = request.POST
    grocery_item = Grocery_item.objects.get(pk=id)

    grocery_item.completed = not grocery_item.completed
    grocery_item.completed_date = timezone.now()
    grocery_item.save()

    print(grocery_item.completed)
    return HttpResponseRedirect(reverse('grocery_list:index'))


def delete_item(request, id):
    grocery_item = Grocery_item.objects.get(pk =id)
    grocery_item.delete()

    return HttpResponseRedirect(reverse('grocery_list:index'))






    
