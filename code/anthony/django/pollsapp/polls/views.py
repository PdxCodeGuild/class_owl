from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.utils import timezone

from .models import Question, Choice

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')

    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        question = ''
    context = {
        'question': question
    }

    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        form = request.POST
        print(form)
        selected_choice = question.choice_set.get(pk=form['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': 'Get it together and make a selection.'
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def add_question(request):
    if request.method == 'GET':
        return render(request, 'polls/add_question.html')
    elif request.method == 'POST':
        question = Question(question_text=request.POST['question'],
                            pub_date=timezone.now())
        question.save()

        form = request.POST

        for key in form:
            if key.startswith('choice'):
                if len(form[key]) > 3:
                    choice = Choice(question=question,
                                    choice_text=form[key])
                    choice.save()
        return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))
