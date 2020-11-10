from posts.views import public_dash
from django.urls import path
from . import views

app_name = 'posts'


urlpatterns= [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_post/', views.create_post, name='create_post'),
    path('public_dash/<int:chirp_id>', views.public_dash, name="public_dash"),
    path('likes/<int:num>/', views.likes, name='likes'),
    path('delete_post/<int:chirp_id>', views.delete_post, name='delete_post')

]

