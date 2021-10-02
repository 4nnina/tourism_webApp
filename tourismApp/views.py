from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
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

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('logIn')
        else:
            messages.info(request, 'Password not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')

def logIn(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credential invalid')
            return redirect('logIn')
    else:
        return render(request, 'login.html')

def logOut(request):
    auth.logout(request)
    return redirect('/')

def edit(request):
    return render(request, 'edit.html')

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