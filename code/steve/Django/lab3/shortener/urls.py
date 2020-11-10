from django.urls import path
from . import views

app_name = "shortener"
urlpatterns = [
    path('', views.index, name="index"),
    path('get_urls/', views.get_urls, name="get_urls"),
    path('post_urls/', views.post_urls, name="post_urls"),
    path('<str:code>/', views.go_to_urls, name="go_to_urls"),
]