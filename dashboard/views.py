from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
        'text': 'Hello, World!'
    }

    return render(request, 'index.html', context)
