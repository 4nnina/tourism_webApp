from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import *
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
    #argument = request.POST[]
    context = {
        'art': Art.objects.order_by('name_it'),
        'category': AArtCategoryArtCategory.objects,
    }
    return render(request, 'edit.html', context)

def item(request,pk):
    art = Art.objects.get(name_it=pk)
    cat = AArtCategoryArtCategory.objects.filter(points=art.classid)
    category = []
    for c in cat:
        category.append(c.category)

    context = {
        'art': art,
        'category': category
    }

    return render(request,'art-details.html', context)

def editArt(request,pk):
    art = Art.objects.get(name_it=pk)

    if request.method == 'POST':
        classid = request.POST['classid']
        descr_it = request.POST['descr_it']
        image_url = request.POST['image_url']
        name_it = request.POST['name_it']
        state = request.POST['state'] #?
        notes = request.POST['notes']
        open_time = request.POST['open_time']
        tickets = request.POST['tickets']
        rss = request.POST['rss']
        saving_vc = request.POST['saving_vc']
        vc = request.POST['vc']
        vc_id = request.POST['vc_id']

        if art.descr_it != descr_it:
            Art.objects.filter(classid=classid).update(descr_it=descr_it)
        if art.image_url != image_url:
            Art.objects.filter(classid=classid).update(image_url=image_url)
        if art.name_it != name_it:
            Art.objects.filter(classid=classid).update(name_it=name_it)
        if art.state != state:
            Art.objects.filter(classid=classid).update(state=state)
        if art.notes != notes:
            Art.objects.filter(classid=classid).update(notes=notes)
        if art.open_time != open_time:
            Art.objects.filter(classid=classid).update(open_time=open_time)
        if art.tickets != tickets:
            Art.objects.filter(classid=classid).update(tickets=tickets)
        if art.rss != rss:
            Art.objects.filter(classid=classid).update(rss=rss)
        if art.saving_vc != saving_vc:
            Art.objects.filter(classid=classid).update(saving_vc=saving_vc)
        if art.vc != vc:
            Art.objects.filter(classid=classid).update(vc=vc)
        if art.vc_id != vc_id:
            Art.objects.filter(classid=classid).update(vc_id=vc_id)

        return redirect('/{}'.format(pk))

    context = {
        'art' : art,
    }

    return render(request,'editArt.html', context)

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
    if request.method == 'POST':
        category = {}
        category_t = {}
        art = {}


        cat = request.POST.getlist('category[]')
        print(cat)
        for i in range(len(cat)):
            print()
            if cat[i-1] is True:
                print('im in')
                category.append(ArtCategory.objects.filter(classid=i))
                category_t.append(AArtCategoryArtCategory.objects.filter(category=i))

        for c in category_t:
            art.append(Art.objects.filter(name_it=c.points))

        context = {
            'art': art,
            'category_t': category_t,
            'category': category,
        }
        print('if')
        return redirect('index')
        #return render(request, 'index.html',context)
    else:
        context = {
            'art': Art.objects.order_by('name_it'),
            'category_t': AArtCategoryArtCategory.objects,
            'category': ArtCategory.objects.order_by('classid'),
        }
    return render(request, 'index.html',context)