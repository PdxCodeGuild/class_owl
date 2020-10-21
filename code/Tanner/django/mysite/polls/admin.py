from django.contrib import admin
from .models import Question

from django.contrib import admin
from .models import Question, Choice
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)