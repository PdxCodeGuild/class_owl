from django.urls import path
from . import views

app_name = 'posts'



urlpatterns = [
    path('', views.index, name='index')
    #path('post/', views.post_chirp, name="post_chirp"),
]
