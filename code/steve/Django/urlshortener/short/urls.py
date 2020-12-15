from django.urls import path
from . import views

app_name = "short"
urlpatterns = [
    path('', views.index, name='index'),
    path('shortener/', views.shortener, name='shortener'),
    path('saver/', views.saver, name='saver'),
    path('redirect/', views.redirector, name='redirector'),
    path('shortlist/', views.shortlist, name='shortlist'),
]