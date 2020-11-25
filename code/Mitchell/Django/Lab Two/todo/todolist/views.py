from django.shortcuts import render, HttpResponse
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.order_by('-priority')
    context = {
        'todos': todos
    }
    return render(request, 'todo/index.html', context)