from django.urls import path
from . import views

app_name="GroceryList"
urlpatterns = [
    path('', views.index, name="index"),
    path('save_GroceryList/', views.save_GroceryList, name="save_GroceryList"),
    path('toggle_complete/<int:GroceryList_id>/', views.toggle_complete, name='toggle_complete'),
    path('delete/<int:GroceryList_id>/', views.delete, name="delete")

]