from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'housing.html', context)

