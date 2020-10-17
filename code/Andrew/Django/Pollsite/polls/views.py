from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template import context
from .models import Question
# Create your views here.
# Ste 3 at the exceptions portion

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ", ".join([q.question_text for q in latest_question_list])

    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }



    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at quesiton %s." % question_id)

def results(request, question_id):
    response = "You're Looking at the results of question %s."
    return HttpResponse( response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)