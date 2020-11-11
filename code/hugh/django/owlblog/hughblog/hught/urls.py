from django.urls import path

from . import views
from  import users

app_name= 'hught'
urlpatterns = [
    path('',views.index,name='index'),
    path('save_hught/', views.save_hught, name="save_hught"),
    path('delete_hught/<int:hught_id>/', views.delete_hught, name="delete_hught"),
    path('users/', users.views, name='login')
]
