from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.order_by('-priority')
    context = {
        'todos': todos
    }
    return render(request, 'todo/index.html', context)

def save_todo(request):
    form = request.POST

    todo = Todo(task=form['todo_task'], priority=form['priority'])
    todo.save()

    return HttpResponseRedirect(reverse('todo:index'))

def toggle_complete(request, todo_id):
    todo = Todo.objects.get(pk= todo_id)
    todo.completed = not todo.completed

    if todo.completed:
        todo.date_completed = timezone.now()

    todo.save()
    return HttpResponseRedirect(reverse('todo:index'))

def delete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('todo:index'))