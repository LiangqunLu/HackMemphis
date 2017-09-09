from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, this is a housing information page")

    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)


