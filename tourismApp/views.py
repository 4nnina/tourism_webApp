import random
import string

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import *
from .forms import ArtForm
# Create your views here.

def pForm(request):
    context ={
        'form' : ArtForm(),
    }
    return render(request,'pForm.html', context)

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
        #'lang' : Lang.objects.get(active=True),
    }
    return render(request, 'index.html', context)

def itemPoI(request,classid_lang):
    if '+' not in classid_lang:
        classid, lang = classid_lang, 'it'
    else:
        classid, lang = classid_lang.split('+')
    art = Art.objects.get(classid=classid)
    cat = AArtCategoryArtCategory.objects.filter(points=art.classid)
    category = []
    for c in cat:
        category.append(c.category)

    #lang = Lang.objects.get(active=True)

    if lang == 'it':
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

def itemTour(request,classid_lang):
    if '+' not in classid_lang:
        classid, lang = classid_lang, 'it'
    else:
        classid, lang = classid_lang.split('+')
    tour = Tour.objects.get(classid=classid)

    if lang == 'it':
        descr_trad = tour.descr_it
        name_trad = tour.name_it
    else:
        lang_table = DELang.objects.get(code=lang)
        try:
            descr_trad = TourDescrTradT.objects.get(classref=classid, descr_trad_lang=lang_table).descr_trad_value
        except:
            descr_trad = tour.descr_it

        try:
            name_trad = TourNameTradT.objects.get(classref=classid, name_trad_lang=lang_table).name_trad_value
        except:
            name_trad = tour.name_it

    art_tour = AArtTourTour.objects.filter(tour=classid).order_by('num')
    arts = Art.objects.none()
    for a in art_tour:
        arts |= Art.objects.filter(name_it=a.point_of_interest)

    context = {
        'tour': tour,
        'lang' : lang,
        'descr_trad' : descr_trad,
        'name_trad' : name_trad,
        'arts' : arts,
        'category_t': AArtCategoryArtCategory.objects,
        'order' : art_tour.values('num','point_of_interest')
    }

    return render(request,'tour-details.html', context)

def editArt(request):
    context = {
        'art': Art.objects.order_by('name_it'),
        'category': AArtCategoryArtCategory.objects,
    }

    return render(request, 'edit.html', context)

def editTour(request):
    context = {
        'tour': Tour.objects.order_by('name_it'),
    }

    return render(request, 'editTour.html', context)

def editPoI(request, classid_lang):
    if '+' not in classid_lang:
        classid, lang = classid_lang, 'it'
    else:
        classid, lang = classid_lang.split('+')
        de_lang = DELang.objects.get(code=lang)

    art = Art.objects.get(classid=classid)

    if lang == 'it':
        descr = art.descr_it
        name = art.name_it
    else:
        try:
            descr_obj = ArtDescrTradT.objects.get(classref=art.classid, descr_trad_lang=de_lang)
            descr = descr_obj.descr_trad_value
        except:
            descr_obj = ArtDescrTradT()
            descr_obj.classref = art
            descr_obj.descr_trad_lang = de_lang
            descr_obj.descr_trad_value = ""
            descr = descr_obj.descr_trad_value
            descr_obj.save()

        try:
            name_obj = ArtNameTradT.objects.get(classref=art.classid, name_trad_lang=de_lang)
            name = name_obj.name_trad_value
        except:
            name_obj = ArtNameTradT()
            name_obj.classref = art
            name_obj.name_trad_lang = de_lang
            name_obj.name_trad_value = ""
            name = name_obj.name_trad_value
            name_obj.save()

    if request.method == 'POST':

        form = ArtForm(request.POST)

        if form.is_valid():
            descr = form.cleaned_data['descr_it']
            name = form.cleaned_data['name_it']
            image_url = form.cleaned_data['image_url']
            notes = form.cleaned_data['notes']
            open_time = form.cleaned_data['open_time']
            tickets = form.cleaned_data['tickets']
            rss = form.cleaned_data['rss']
            saving_vc = form.cleaned_data['saving_vc']
            vc = form.cleaned_data['vc']
            vc_id = form.cleaned_data['vc_id']

        if lang == 'it':
            if art.name_it != name:
                Art.objects.filter(classid=classid).update(name_it=name)
            if art.descr_it != descr:
                Art.objects.filter(classid=classid).update(descr_it=descr)
        else:
            if name_obj.name_trad_value != name:
                ArtNameTradT.objects.filter(classref=classid, name_trad_lang=de_lang).update(name_trad_value=name)
            if descr_obj.descr_trad_value != descr:
                ArtDescrTradT.objects.filter(classref=classid, descr_trad_lang=de_lang).update(descr_trad_value=descr)

        if image_url != 'None' and art.image_url != image_url:
            Art.objects.filter(classid=classid).update(image_url=image_url)
        if notes != 'None' and art.notes != notes:
            Art.objects.filter(classid=classid).update(notes=notes)
        if open_time != 'None' and art.open_time != open_time:
            Art.objects.filter(classid=classid).update(open_time=open_time)
        if tickets != 'None' and art.tickets != tickets:
            Art.objects.filter(classid=classid).update(tickets=tickets)
        if rss != 'None' and art.rss != rss:
            Art.objects.filter(classid=classid).update(rss=rss)
        if saving_vc != 'None' and art.saving_vc != saving_vc:
            Art.objects.filter(classid=classid).update(saving_vc=saving_vc)
        if vc != 'None' and art.vc != vc:
            Art.objects.filter(classid=classid).update(vc=vc)
        if vc_id != 'None' and art.vc_id != vc_id:
            Art.objects.filter(classid=classid).update(vc_id=vc_id)

        if '_delete' in request.POST:
            Art.objects.filter(classid=classid).update(state='02')

        return redirect('/Art/{}+{}'.format(classid,lang))

    context = {
        'art' : art,
        'lang' : lang,
        'descr' : descr,
        'name' : name,
        'form' : ArtForm(initial={'name_it': name, 'descr_it': descr, 'image_url': art.image_url,
                                'notes': art.notes, 'open_time': art.open_time, 'tickets': art.tickets,
                                'rss': art.rss, 'saving_vc': art.saving_vc, 'vc': art.vc, 'vc_id': art.vc_id})
        #'state':DArtEStato.objects
    }

    return render(request,'editPointOfInterest.html', context)

def editOneTour(request, classid_lang):
    context = {
        'tour' : Tour.objects.get(classid=classid_lang)
    }
    return render(request,'editOneTour.html', context)

def newArt(request):

    if request.method == 'POST':
        #classid = request.POST['classid']

        while True:
            try:
                id = "".join(random.choices(string.digits, k=5))
                Art.objects.get(classid=id)
            except:
                art = Art(classid=id)
                break
        print("codice: ", id)
        form = ArtForm(request.POST)


        if form.is_valid():
            art.descr_it = form.cleaned_data['descr_it']
            art.image_url = form.cleaned_data['image_url']
            art.name_it = form.cleaned_data['name_it']
            art.state = DArtEStato.objects.get(name='attivo')
            art.notes = form.cleaned_data['notes']
            art.open_time = form.cleaned_data['open_time']
            art.tickets = form.cleaned_data['tickets']
            art.rss = form.cleaned_data['rss']
            art.saving_vc = form.cleaned_data['saving_vc']
            art.vc = form.cleaned_data['vc']
            art.vc_id = form.cleaned_data['vc_id']

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

        return redirect('/Art/{}'.format(id))

    context = {
        #'lang': Lang.objects.get(active=True),
        'form': ArtForm()
    }
    return render(request, 'newArt.html',context)

def newTour(request):
    context = {

    }
    return render(request, 'newTour.html', context)

def filterItemArt(request):
    select = [None, True, True, True, True, True, True]
    if request.method == 'POST':

        category = ArtCategory.objects.none()
        category_t = AArtCategoryArtCategory.objects.none()
        art = Art.objects.none()
        cat = 0

        if 'Chiese' in request.POST:
            cat += 1
            select[1] = True
            category |= ArtCategory.objects.filter(classid='1')
            category_t |= AArtCategoryArtCategory.objects.filter(category='1')
        else:
            select[1] = False

        if 'Monumenti' in request.POST:
            cat += 1
            select[2] = True
            category |= ArtCategory.objects.filter(classid='2')
            category_t |= AArtCategoryArtCategory.objects.filter(category='2')
        else:
            select[2] = False

        if 'Teatri' in request.POST:
            cat += 1
            select[3] = True
            category |= ArtCategory.objects.filter(classid='3')
            category_t |= AArtCategoryArtCategory.objects.filter(category='3')
        else:
            select[3] = False

        if 'Musei' in request.POST:
            cat += 1
            select[4] = True
            category |= ArtCategory.objects.filter(classid='4')
            category_t |= AArtCategoryArtCategory.objects.filter(category='4')
        else:
            select[4] = False

        if 'Palazzi' in request.POST:
            cat += 1
            select[5] = True
            category |= ArtCategory.objects.filter(classid='5')
            category_t |= AArtCategoryArtCategory.objects.filter(category='5')
        else:
            select[5] = False

        if 'Archeologici' in request.POST:
            cat += 1
            select[6] = True
            category |= ArtCategory.objects.filter(classid='6')
            category_t |= AArtCategoryArtCategory.objects.filter(category='6')
        else:
            select[6] = False

        for c in category_t:
            art |= Art.objects.filter(name_it=c.points).order_by('name_it')

        context = {
            'art': art,
            'category_t': category_t,
            'category': category,
            'select' : select,
        }
    else:
        context = {
            'art': Art.objects.order_by('name_it'),
            'category_t': AArtCategoryArtCategory.objects,
            'category': ArtCategory.objects.order_by('classid'),
            'select': select,
            #'lang' : Lang.objects.get(active=True),
        }

    return render(request, 'filterArt.html', context)

def filterItemTour(request):
    select = [True, True, True]
    if request.method == 'POST':
        tour = Tour.objects.none()

        if 'tempo' in request.POST:
            select[0] = True
            tour |= Tour.objects.filter(type='a tempo').order_by('name_it')
        else:
            select[0] = False

        if 'tema' in request.POST:
            select[1] = True
            tour |= Tour.objects.filter(type='a tema').order_by('name_it')
        else:
            select[1] = False

        if 'storico' in request.POST:
            select[2] = True
            tour |= Tour.objects.filter(type='storico').order_by('name_it')
        else:
            select[2] = False

        context = {
            'tour': tour,
            'select': select,
        }
    else:
        context ={
            'tour': Tour.objects.order_by('name_it'),
            'select': select,
        }

    return render(request, 'filterTour.html', context)


