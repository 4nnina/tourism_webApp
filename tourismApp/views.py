from django.shortcuts import render, get_object_or_404

from .models import Crowding
# Create your views here.

def homepage(request):
    tab = Crowding.objects
    return render(request, 'homepage.html', {'tab':tab})

def logIn(request):
    return render(request, 'logIn.html')
