from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Crowding
# Create your views here.

def homepage(request):
    #ords = request.GET['text']
    words = request.POST['text']
    context = {
        'tab' : Crowding.objects,
        'n_word' : len(words.split()),
    }
    return render(request, 'homepage.html', context)

def logIn(request):
    return render(request, 'logIn.html')

def example(request):
    context = {
        'name':'Patrick',
        'age':23,
        'nationality':'British',
    }
    return render(request,'example.html', context)

'''
def index(request):
    return HttpResponse('<h1> hello </h1>')
'''

def index(request):
    return render(request, 'index.html')