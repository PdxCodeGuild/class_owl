from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import MyModel

from .models import Conversation, Comment



# Create your views here.

def index(request):
    conversations = Conversation.objects.order_by('title')[:5]

    context = {
        'conversations': conversations,
    }
    return render(request, 'void/index.html', context)

def recording(request):
    # return redirect('void:recording')

    return render(request, 'void/recording.html')

@login_required
def create(request):

    if request.method == "POST":
        form = request.POST
        title = form['title']
        body = form['body']
        image_url = form['image']
        published = form.get('publish', False)
        author = request.user
        voicefile = request.FILES.get("recording_file")
        

        if published:
            published = True
            date_published = timezone.now()
            conversation = Conversation(title=title, body=body, author=author,
                        published_date=date_published, image=image_url, voicefile=voicefile)
        else:
            conversation = Conversation(title=title, body=body,
                        author=author, image=image_url, voicefile=voicefile)

        conversation.save()
        return redirect('users:dashboard')

    return render(request, 'void/create.html')


def detail(request, conversation_id):
    conversation = Conversation.objects.get(pk=conversation_id)
    context = {
        'Conversation': conversation
    }
    return render(request, 'void/detail.html', context)


@login_required
def delete_conversation(request, conversation_id):
    conversation = Conversation.objects.get(pk=conversation_id)

    user = request.user
    if user == conversation.author:
        conversation.delete()

    return redirect('users:dashboard')


@login_required
def comment(request, conversation_id):
    conversation = Conversation.objects.get(pk=conversation_id)
    form = request.POST
    body = form['comment_body']
    comment = Comment(body=body, author=request.user, conversation=conversation)

    comment.save()

    return redirect('void:detail', conversation_id=conversation_id)


@login_required
def like(request):
    params = request.GET

    opinion = params['opinion']
    interest = params['interest']
    id = int(params['id'])

    if interest == 'comment':
        comment = Comment.objects.get(pk=id)
        if opinion == 'like':
            comment.likes += 1
        else:
            comment.dislikes += 1
        comment.save()
        id = comment.conversation.id
    elif interest == 'conversation':
        conversation = Conversation.objects.get(pk=id)
        if opinion == 'like':
            conversation.likes += 1
            conversation.total_likes += 1
        else:
            conversation.dislikes += 1
            conversation.total_likes -= 1
        conversation.save()

    return redirect('void:detail', conversation_id=id)


@login_required
def upload_file(request):
        recording_file = request.FILES['recording_file']
        model = MyModel(..., recording_file=recording_file)
        model.save()
