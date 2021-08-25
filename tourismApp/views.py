from django.shortcuts import render, get_object_or_404

from .models import AArtTourTour
# Create your views here.

def homepage(request):
    tab = AArtTourTour.objects
    return render(request, 'homepage.html', {'tab':tab})
