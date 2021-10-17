from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import *

# Create your views here.

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

def index(request):
    context = {
        'lang' : Lang.objects.get(active=True),
    }
    return render(request, 'index.html', context)

def item(request,pk):
    art = Art.objects.get(classid=pk)
    cat = AArtCategoryArtCategory.objects.filter(points=art.classid)
    category = []
    for c in cat:
        category.append(c.category)

    lang = Lang.objects.get(active=True)

    if lang.code == 'it':
        descr_trad = art.descr_it
        name_trad = art.name_it
    else:
        lang_table = DELang.objects.get(code=lang)
        try:
            descr_trad = ArtDescrTradT.objects.get(classref=art.classid, descr_trad_lang=lang_table).descr_trad_value
        except:
            descr_trad = art.descr_it

        try:
            name_trad = ArtNameTradT.objects.get(classref=art.classid, name_trad_lang=lang_table).name_trad_value
        except:
            name_trad = art.name_it

    context = {
        'art': art,
        'category': category,
        'lang' : lang,
        'descr_trad' : descr_trad,
        'name_trad' : name_trad,
    }

    return render(request,'art-details.html', context)

def edit(request):
    context = {
        'art': Art.objects.order_by('name_it'),
        'category': AArtCategoryArtCategory.objects,
        'lang' : Lang.objects.get(active=True),
    }

    return render(request, 'edit.html', context)

def editArt(request,pk):
    art = Art.objects.get(classid=pk)

    if request.method == 'POST':
        classid = request.POST['classid']
        descr_it = request.POST['descr_it']
        image_url = request.POST['image_url']
        name_it = request.POST['name_it']
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

        if '_delete' in request.POST:
            Art.objects.filter(classid=classid).update(state='02')

        return redirect('/{}'.format(classid))

    context = {
        'art' : art,
        'lang' : Lang.objects.get(active=True),
        #'state':DArtEStato.objects
    }

    return render(request,'editArt.html', context)


def newArt(request):

    if request.method == 'POST':
        classid = request.POST['classid']


        if Art.objects.filter(classid=classid).exists():
            messages.info(request, 'Classid {} already exist'.format(classid))
            return render(request, 'newArt.html')
        else:
            art = Art(classid=classid)

            descr_it = request.POST['descr_it']
            if descr_it:
                art.descr_it = descr_it

            image_url = request.POST['image_url']
            if image_url:
                art.image_url = image_url

            name_it = request.POST['name_it']
            if name_it:
                art.name_it = name_it
            else:
                messages.info(request, 'Name_it required')
                return render(request, 'newArt.html')

            state = request.POST['state']
            art.state = DArtEStato.objects.get(code=state)

            notes = request.POST['notes']
            if notes:
                art.notes = notes

            open_time = request.POST['open_time']
            if open_time:
                art.open_time = open_time

            tickets = request.POST['tickets']
            if tickets:
                art.tickets = tickets

            rss = request.POST['rss']
            if rss:
                art.rss = rss

            saving_vc = request.POST['saving_vc']
            if saving_vc:
                art.saving_vc = saving_vc

            vc = request.POST['vc']
            if vc:
                art.vc = vc

            vc_id = request.POST['vc_id']
            if vc_id:
                art.vc_id = vc_id

            #art = Art(classid=classid, descr_it=descr_it, image_url=image_url, name_it=name_it,state=DArtEStato_var, notes=notes, open_time=open_time, tickets=tickets,rss=rss, vc_id=vc_id)

            art.save()

            if 'Chiese' in request.POST:
                cat = ArtCategory.objects.get(classid='1')
                category_t = AArtCategoryArtCategory(category=cat, points=art)
                category_t.save()
            if 'Monumenti' in request.POST:
                cat = ArtCategory.objects.get(classid='2')
                category_t = AArtCategoryArtCategory(category=cat, points=art)
                category_t.save()
            if 'Teatri' in request.POST:
                cat = ArtCategory.objects.get(classid='3')
                category_t = AArtCategoryArtCategory(category=cat, points=art)
                category_t.save()
            if 'Musei' in request.POST:
                cat = ArtCategory.objects.get(classid='4')
                category_t = AArtCategoryArtCategory(category=cat, points=art)
                category_t.save()
            if 'Palazzi' in request.POST:
                cat = ArtCategory.objects.get(classid='5')
                category_t = AArtCategoryArtCategory(category=cat, points=art)
                category_t.save()
            if 'Archeologici' in request.POST:
                cat = ArtCategory.objects.get(classid='6')
                category_t = AArtCategoryArtCategory(category=cat, points=art)
                category_t.save()

            return redirect('/{}'.format(name_it))
    context = {
        'lang': Lang.objects.get(active=True),
    }
    return render(request, 'newArt.html',context)


def filterItemArt(request):
    if request.method == 'POST':
        category = ArtCategory.objects.none()
        category_t = AArtCategoryArtCategory.objects.none()
        art = Art.objects.none()

        if 'Chiese' in request.POST:
            category |= ArtCategory.objects.filter(classid='1')
            category_t |= AArtCategoryArtCategory.objects.filter(category='1')

        if 'Monumenti' in request.POST:
            category |= ArtCategory.objects.filter(classid='2')
            category_t |= AArtCategoryArtCategory.objects.filter(category='2')

        if 'Teatri' in request.POST:
            category |= ArtCategory.objects.filter(classid='3')
            category_t |= AArtCategoryArtCategory.objects.filter(category='3')

        if 'Musei' in request.POST:
            category |= ArtCategory.objects.filter(classid='4')
            category_t |= AArtCategoryArtCategory.objects.filter(category='4')

        if 'Palazzi' in request.POST:
            category |= ArtCategory.objects.filter(classid='5')
            category_t |= AArtCategoryArtCategory.objects.filter(category='5')

        if 'Archeologici' in request.POST:
            category |= ArtCategory.objects.filter(classid='6')
            category_t |= AArtCategoryArtCategory.objects.filter(category='6')

        for c in category_t:
            art |= Art.objects.filter(name_it=c.points)

        context = {
            'art': art,
            'category_t': category_t,
            'category': category,
        }
    else:
        context = {
            'art': Art.objects.order_by('name_it'),
            'category_t': AArtCategoryArtCategory.objects,
            'category': ArtCategory.objects.order_by('classid'),            'lang' : Lang.objects.get(active=True),
        }

    return render(request, 'filterArt.html', context)

def filterItemTour(request):
    context ={
        'lang': Lang.objects.get(active=True),
    }
    return render(request, 'filterTour.html', context)


