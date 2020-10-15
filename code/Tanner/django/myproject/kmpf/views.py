from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'message': 'apple bottom jeans'
    }
    return render(request, 'kmpf/index.html', context)

def about(request):
    context = {
        'message': 'hi'
    }  

    return render(request, 'kmpf/about.html', context)
    