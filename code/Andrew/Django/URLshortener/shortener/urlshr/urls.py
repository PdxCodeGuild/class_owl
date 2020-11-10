from django.urls import path
from . import views


app_name = 'urlshr'

urlpatterns = [
    path('', views.index, name='index'),
    path('shorten/', views.shorten, name='shorten'),
    path('go_to_site/<str:id>', views.go_to_site, name='go_to_site')

]