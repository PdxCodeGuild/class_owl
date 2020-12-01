from django.urls import path
from . import views

app_name="todo"
urlpatterns = [
    path('', views.index, name="index"),
    path('save_todo/', views.save_todo, name="save_todo"),
    path('toggle_complete/<int:todo_id>/', views.toggle_complete, name='toggle_complete'),
    path('delete/<int:todo_id>/', views.delete, name="delete")

]