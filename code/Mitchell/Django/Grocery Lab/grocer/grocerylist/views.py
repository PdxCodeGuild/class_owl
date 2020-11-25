from django.shortcuts import render
from .models import Glist


# Create your views here.
def index(request):
    grocery_list = Glist.objects
    context = {
        'grocery_list': grocery_list
    }
    return render(request, 'grocerylist/index.html', context)