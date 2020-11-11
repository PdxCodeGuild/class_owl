from . import views
from django.urls import path

app_name='shortener'
urlpatterns=[
    path('',views.index, name='index'),
    path('get_urls/', views.get_urls, name='get_urls'),
    path('post_urls/', views.post_urls, name='post_urls')
]