from django.contrib import admin
from . models import Conversation, Comment

# Register your models here.
admin.site.register(Conversation)
admin.site.register(Comment)