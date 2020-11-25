from django.urls import path

from . import views

app_name = "void"
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:conversation_id>/', views.detail, name='detail'),
    path('delete/<int:conversation_id>/', views.delete_conversation, name='delete'),
    path('comment/<int:conversation_id>/', views.comment, name='comment'),
    path('like/', views.like, name='like'),
    path('recording/', views.recording, name="recording")
]