from django.urls import path
from . import views

app_name="grocery"
urlpatterns = [
    path('', views.index, name="index"),
    path('save_grocery/', views.save_grocery, name="save_grocery"),
    path('toggle_complete/<int:grocery_id>/', views.toggle_complete, name='toggle_complete'),
    path('delete/<int:grocery_id>/', views.delete, name="delete"),
]
