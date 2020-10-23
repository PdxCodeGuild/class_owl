from django.urls import path
from . import views

app_name = 'grocery_list'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('add_item/', views.add_item, name="add_item"),
    path('completed_item/<int:id>/', views.completed_item, name='completed_item'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item')
]