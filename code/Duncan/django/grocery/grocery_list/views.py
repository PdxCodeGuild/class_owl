from django.shortcuts import render
from django.http import HttpResponse
from .models import groceryItem
# Create your views here.


def index(request):
    items = groceryItem
    context = {
        'items': items,
        'message': "Groceries"
    }
    return render(request, 'grocery_list/index.html', context)