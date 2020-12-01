from django.urls import path
from . import views

app_name = 'grocerylist'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('grocerylist/', views.save_list_item, name='save_list_item'),
    path('toggle_complete/<int:list_item_id>/', views.toggle_complete, name='toggle_complete'),
    path('delete/<int:list_item_id>/', views.delete, name="delete")

]