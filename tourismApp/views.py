import random
import string

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db import transaction
from django.contrib.gis.geos import Point

from .models import *
from .forms import *

# Create your views here.

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

    try:
        art = Art.objects.get(classid=classid)
    except:
        print('except itemPoi Art')
        art = Art()

    cat = AArtCategoryArtCategory.objects.filter(points=art.classid)
    category = []
    for c in cat:
        category.append(c.category)

    #lang = Lang.objects.get(active=True)

    if lang == 'it':
        descr_trad = art.descr_it
        name_trad = art.name_it
        tickets_trad = art.tickets
        open_time_trad = art.open_time
    else:
        lang_table = DELang.objects.get(code=lang)
        try:
            descr_trad = ArtDescrTradT.objects.get(classref=art.classid, descr_trad_lang=lang_table).descr_trad_value
        except:
            descr_trad = '<b style="color:red;">Non ancora tradotto in {}</b>'.format(lang_table.name)

        try:
            name_trad = ArtNameTradT.objects.get(classref=art.classid, name_trad_lang=lang_table).name_trad_value
        except:
            name_trad = art.name_it

        try:
            trad = ArtTradT.objects.get(classref=art.classid, lang=lang_table.code)
            tickets_trad = trad.tickets_trad
            open_time_trad = trad.open_time_trad
        except:
            tickets_trad = '<b style="color:red;">Non ancora tradotto in {}</b>'.format(lang_table.name)
            open_time_trad = '<b style="color:red;">Non ancora tradotto in {}</b>'.format(lang_table.name)
    try:
        location = Location.objects.get(event=art.classid, num='1')
        longitude, latitude = location.geom
        address = location.address
    except:
        longitude, latitude = None, None
        address = None
    context = {
        'art': art,
        'category': category,
        'lang' : lang,
        'descr_trad' : descr_trad,
        'name_trad' : name_trad,
        'tickets_trad': tickets_trad,
        'open_time_trad': open_time_trad,
        'latitude': latitude,
        'longitude': longitude,
        'address': address,
    }

    return render(request,'art-details.html', context)

def itemTour(request,classid_lang):
    if '+' not in classid_lang:
        classid, lang = classid_lang, 'it'
    else:
        classid, lang = classid_lang.split('+')

    try:
        tour = Tour.objects.get(classid=classid)
    except:
        print('except itemTour Tour')
        tour = Tour()

    if lang == 'it':
        descr_trad = tour.descr_it
        name_trad = tour.name_it
    else:
        lang_table = DELang.objects.get(code=lang)
        try:
            descr_trad = TourDescrTradT.objects.get(classref=classid, descr_trad_lang=lang_table).descr_trad_value
        except:
            descr_trad = '<b style="color:red;">Non ancora tradotto in {}</b>'.format(lang_table.name)

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

def editPoI1(request, classid):
    category = ArtCategory.objects.order_by('classid')
    select = [None, False, False, False, False, False, False, False, False]
    for c in AArtCategoryArtCategory.objects.filter(points=classid):
        select[int(c.category.classid)] = True

    try:
        art = Art.objects.get(classid=classid)
    except:
        print('except editPoI1 Art')
        art = Art()

    try:
        location = Location.objects.get(event=classid, num='1')
        longitude, latitude = location.geom
        address = location.address
        new_location = False
    except:
        new_location = True
        while True:
            try:
                id = "".join(random.choices(string.digits, k=5))
                Location.objects.get(classid=id)
            except:
                location = Location(classid=id, address=None, event=classid, num='1', geom=None)
                latitude = ""
                longitude = ""
                address = ""
                break


    if request.method == 'POST':

        form = ArtForm_data(request.POST)
        locationForm = LocationForm(request.POST)

        if '_delete' in request.POST:
            Art.objects.filter(classid=classid).update(state='02')
            return redirect('editArt')

        if form.is_valid() and locationForm.is_valid():
            image_url = form.cleaned_data['image_url']
            notes = form.cleaned_data['notes']
            saving_vc = form.cleaned_data['s_vc_perc'] / 100 if form.cleaned_data['s_vc_perc'] != 0 else 0.0
            vc = form.cleaned_data['vc']
            vc_id = form.cleaned_data['vc_id']
            address = locationForm.cleaned_data['address']
            latitude = locationForm.cleaned_data['latitude']
            longitude = locationForm.cleaned_data['longitude']

            with transaction.atomic():
                if image_url != 'None' and art.image_url != image_url:
                    Art.objects.filter(classid=classid).update(image_url=image_url)
                if notes != 'None' and art.notes != notes:
                    Art.objects.filter(classid=classid).update(notes=notes)
                if art.saving_vc != saving_vc:
                    Art.objects.filter(classid=classid).update(saving_vc=saving_vc)
                if vc != 'None' and art.vc != vc:
                    Art.objects.filter(classid=classid).update(vc=vc)
                if vc_id != 'None' and art.vc_id != vc_id:
                    Art.objects.filter(classid=classid).update(vc_id=vc_id)
                if new_location:
                    location.address = address
                    location.geom = Point(float(longitude), float(latitude))
                    location.save()
                else:
                    if address != location.address:
                        Location.objects.filter(event=classid, num='1').update(address=address)
                    if (longitude,latitude) != location.geom:
                        Location.objects.filter(event=classid, num='1').update(geom=Point(float(longitude),
                                                                                          float(latitude)))


                for c in range(1, len(category) + 1):
                    if 'categoria_{}'.format(c) in request.POST:
                        if select[c]:
                            select[c] = None
                        elif not select[c]:
                            newArtCat = AArtCategoryArtCategory(points=art, category=ArtCategory.objects.get(classid=str(c)))
                            newArtCat.save()
                    else:
                        if select[c]:
                            AArtCategoryArtCategory.objects.get(points=art, category=ArtCategory.objects.get(classid=str(c))).delete()


        return redirect('/edit/translation/{}'.format(classid))

    context = {
        'art' : art,
        'category': category,
        'select': select,
        'de_vc': DEVc.objects.order_by('code').reverse(),
        'form' : ArtForm_data(initial={'image_url': art.image_url, 'notes': art.notes,
                                       's_vc_perc': art.saving_vc*100, 'vc': art.vc, 'vc_id': art.vc_id}),
        'locationForm': LocationForm(initial={'address': address, 'latitude':latitude, 'longitude': longitude}),
        'address': address,
        'latitude': latitude,
        'longitude': longitude,
        #'state':DArtEStato.objects
    }
    return render(request,'editPointOfInterest.html', context)

def editPoI2(request, classid_lang):
    if '+' not in classid_lang:
        classid, lang = classid_lang, 'it'
    else:
        classid, lang = classid_lang.split('+')
        de_lang = DELang.objects.get(code=lang)

    art = Art.objects.get(classid=classid)

    if lang == 'it':
        descr = art.descr_it
        name = art.name_it
        tickets = art.tickets
        open_time = art.open_time
        #notes = art.notes
        translated = True
    else:
        translated = False
        try:
            descr_obj = ArtDescrTradT.objects.get(classref=art.classid, descr_trad_lang=de_lang)
            descr = descr_obj.descr_trad_value
            descr_t = True
        except:
            descr_t = False
            descr_obj = ArtDescrTradT()
            descr_obj.classref = art
            descr_obj.descr_trad_lang = de_lang
            descr_obj.descr_trad_value = ""
            descr = descr_obj.descr_trad_value
            #descr_obj.save()

        try:
            name_obj = ArtNameTradT.objects.get(classref=art.classid, name_trad_lang=de_lang)
            name = name_obj.name_trad_value
            name_t = True
        except:
            name_t = False
            name_obj = ArtNameTradT()
            name_obj.classref = art
            name_obj.name_trad_lang = de_lang
            name_obj.name_trad_value = ""
            name = name_obj.name_trad_value
            #name_obj.save()

        try:
            trad_obj = ArtTradT.objects.get(classref=art.classid, lang=de_lang.code)
            tickets = trad_obj.tickets_trad
            open_time = trad_obj.open_time_trad
            #notes = trad_obj.notes_trad
            trad_t = True
        except:
            trad_t = False
            trad_obj = ArtTradT()
            trad_obj.classref = art
            trad_obj.lang = de_lang.code
            trad_obj.tickets_trad = ""
            tickets = trad_obj.tickets_trad
            trad_obj.open_time_trad = ""
            open_time = trad_obj.open_time_trad
            #notes = None

    if request.method == 'POST':

        form = ArtForm_Trad(request.POST)

        if form.is_valid():
            descr = form.cleaned_data['descr_it']
            name = form.cleaned_data['name_it']
            tickets = form.cleaned_data['tickets']
            open_time = form.cleaned_data['open_time']
            #notes = form.cleaned_data['notes']
        else:
            if 'open_time' in form.errors:
                messages.info(request, 'Field Open time is too long!')
                context = {
                    'art': art,
                    'lang': lang,
                    'descr': descr,
                    'name': name,
                    'de_vc': DEVc.objects.order_by('code').reverse(),
                    'form': ArtForm_Trad(
                        initial={'name_it': name, 'descr_it': descr, 'open_time': open_time, 'tickets': tickets, })
                    # 'state':DArtEStato.objects
                }

                return render(request, 'editPoiTranslate.html', context)
            elif 'tickets' in form.errors:
                messages.info(request, 'Field Tickets is too long!')
                context = {
                    'art': art,
                    'lang': lang,
                    'descr': descr,
                    'name': name,
                    'de_vc': DEVc.objects.order_by('code').reverse(),
                    'form': ArtForm_Trad(
                        initial={'name_it': name, 'descr_it': descr, 'open_time': open_time, 'tickets': tickets, })
                    # 'state':DArtEStato.objects
                }

                return render(request, 'editPoiTranslate.html', context)

        with transaction.atomic():
            if not translated:
                if not name_t:
                    name_obj.save()
                if not descr_t:
                    descr_obj.save()
                if not trad_t:
                 trad_obj.save()

            if lang == 'it':
                if art.name_it != name:
                    Art.objects.filter(classid=classid).update(name_it=name)
                if art.descr_it != descr:
                    Art.objects.filter(classid=classid).update(descr_it=descr)
                #if art.notes != notes:
                #    Art.objects.filter(classid=classid).update(notes=notes)
                if art.open_time != open_time:
                    Art.objects.filter(classid=classid).update(open_time=open_time)
                if art.tickets != tickets:
                    Art.objects.filter(classid=classid).update(tickets=tickets)
            else:
                if name_obj.name_trad_value != name:
                    ArtNameTradT.objects.filter(classref=classid, name_trad_lang=de_lang).update(name_trad_value=name)
                if descr_obj.descr_trad_value != descr:
                    ArtDescrTradT.objects.filter(classref=classid, descr_trad_lang=de_lang).update(descr_trad_value=descr)
                #if trad_obj.notes_trad != notes:
                #    ArtTradT.objects.filter(classref=classid).update(notes_trad=notes)
                if trad_obj.open_time_trad != open_time:
                    ArtTradT.objects.filter(classref=classid, lang=de_lang.code).update(open_time_trad=open_time)
                if trad_obj.tickets_trad != tickets:
                    ArtTradT.objects.filter(classref=classid, lang=de_lang.code).update(tickets_trad=tickets)

            if '_save' in request.POST:
                return redirect('/Art/{}+{}'.format(classid,lang))
            if '_continue' in request.POST:
                if lang=='it':
                    return redirect('/edit/translation/{}+{}'.format(classid, 'en'))
                de_lang = DELang.objects.order_by('name')
                if lang == 'en':
                    found = True
                else:
                    found = False
                for l in de_lang:
                    if l.code != 'en' and found:
                        return redirect('/edit/translation/{}+{}'.format(classid, l.code))
                    if l.code == lang:
                        found = True
                return redirect('/Art/{}+{}'.format(classid, lang))

    context = {
        'art' : art,
        'lang' : lang,
        'descr' : descr,
        'name' : name,
        'de_vc': DEVc.objects.order_by('code').reverse(),
        'form' : ArtForm_Trad(initial={'name_it': name, 'descr_it': descr, 'open_time': open_time, 'tickets': tickets,})
        #'state':DArtEStato.objects
    }

    return render(request,'editPoiTranslate.html', context)

def editOneTour(request, classid_lang):
    if '+' not in classid_lang:
        classid, lang = classid_lang, 'it'
    else:
        classid, lang = classid_lang.split('+')
        de_lang = DELang.objects.get(code=lang)

    tour = Tour.objects.get(classid=classid)

    if lang == 'it':
        descr = tour.descr_it
        name = tour.name_it
    else:
        try:
            descr_obj = TourDescrTradT.objects.get(classref=tour.classid, descr_trad_lang=de_lang)
            descr = descr_obj.descr_trad_value
        except:
            descr_obj = TourDescrTradT()
            descr_obj.classref = tour
            descr_obj.descr_trad_lang = de_lang
            descr_obj.descr_trad_value = ""
            descr = descr_obj.descr_trad_value
            descr_obj.save()

        try:
            name_obj = TourNameTradT.objects.get(classref=tour.classid, name_trad_lang=de_lang)
            name = name_obj.name_trad_value
        except:
            name_obj = TourNameTradT()
            name_obj.classref = tour
            name_obj.name_trad_lang = de_lang
            name_obj.name_trad_value = ""
            name = name_obj.name_trad_value
            name_obj.save()

    if request.method == 'POST':
        form = TourForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name_it']
            type = DTourETipoit.objects.get(name=form.cleaned_data['type'])
            descr = form.cleaned_data['descr_it']
            image_url = form.cleaned_data['image_url']
            duration = form.cleaned_data['duration']
            #length = form.cleaned_data['length']

        if lang == 'it':
            if tour.name_it != name:
                Tour.objects.filter(classid=classid).update(name_it=name)
            if tour.descr_it != descr:
                Tour.objects.filter(classid=classid).update(descr_it=descr)
        else:
            if name_obj.name_trad_value != name:
                TourNameTradT.objects.filter(classref=classid, name_trad_lang=de_lang).update(name_trad_value=name)
            if descr_obj.descr_trad_value != descr:
                TourDescrTradT.objects.filter(classref=classid, descr_trad_lang=de_lang).update(descr_trad_value=descr)

        if tour.type != type:
            Tour.objects.filter(classid=classid).update(type=type)
        if image_url != 'None' and tour.image_url != image_url:
            Tour.objects.filter(classid=classid).update(image_url=image_url)
        if duration != 'None' and tour.duration != duration:
            Tour.objects.filter(classid=classid).update(duration=duration)
        #if length != 'None' and tour.length != length:
        #    Tour.objects.filter(classid=classid).update(length=length)

        if '_editPOI' in request.POST:
            return redirect('/edit/tour/{}/points'.format(classid,lang))
        if '_save' in request.POST:
            return redirect('/Tour/{}+{}'.format(classid,lang))

    context = {
        'lang' : lang,
        'tour' : tour,
        'form' : TourForm(initial={'name_it': name, 'type': tour.type, 'descr_it': descr, 'image_url': tour.image_url,
                                   'kml_path': tour.kml_path, 'duration': tour.duration, 'length': tour.length}),
    }
    return render(request,'editOneTour.html', context)

def editTourPoi(request,classid):
    poi_in_Tour = AArtTourTour.objects.filter(tour=classid).order_by('num')
    if request.method == 'POST':
        #poi_in_Tour = AArtTourTour.objects.filter(tour=classid)
        number_poi = len(poi_in_Tour)
        if '_add' in request.POST:
            poi = Art.objects.get(classid=request.POST['art'])

            art_tour = AArtTourTour(point_of_interest=poi, tour=Tour.objects.get(classid=classid), num=number_poi + 1)
            art_tour.save()

            return redirect('/edit/tour/{}/points'.format(classid))

        for d in range(1,number_poi+1):
            if '_delete{}'.format(d) in request.POST:
                with transaction.atomic():
                    obj = AArtTourTour.objects.get(num=d, tour=classid)
                    obj.delete()

                    for num in range(d+1, number_poi+1):
                        AArtTourTour.objects.filter(num=num, tour=classid).update(num=num-1)

                return redirect('/edit/tour/{}/points'.format(classid))

            if '_up{}'.format(d) in request.POST:
                first = d - 1
                second = d
                with transaction.atomic():
                    obj1 = AArtTourTour.objects.get(num=first, tour=classid)
                    obj2 = AArtTourTour.objects.get(num=second, tour=classid)
                    AArtTourTour.objects.filter(point_of_interest=obj1.point_of_interest,tour=classid).update(num=second)
                    AArtTourTour.objects.filter(point_of_interest=obj2.point_of_interest,tour=classid).update(num=first)

                return redirect('/edit/tour/{}/points'.format(classid))

            if '_down{}'.format(d) in request.POST:
                first = d
                second = d + 1
                with transaction.atomic():
                    obj1 = AArtTourTour.objects.get(num=first, tour=classid)
                    obj2 = AArtTourTour.objects.get(num=second, tour=classid)
                    AArtTourTour.objects.filter(point_of_interest=obj1.point_of_interest, tour=classid).update(
                        num=second)
                    AArtTourTour.objects.filter(point_of_interest=obj2.point_of_interest, tour=classid).update(
                        num=first)

                return redirect('/edit/tour/{}/points'.format(classid))

        if '_save' in request.POST:
            num = 0
            try:
                for poi in dict(request.POST)['poi']:
                    num += 1
                    obj = AArtTourTour.objects.get(num=num, tour=classid)
                    if obj.point_of_interest.classid != poi:
                        with transaction.atomic():
                            newPoi = Art.objects.get(classid=poi).name_it
                            obj.delete()
                            art_tour = AArtTourTour(point_of_interest=Art.objects.get(classid=poi),
                                                    tour=Tour.objects.get(classid=classid),num=num)

                            try:
                                art_tour.save()
                            except:
                                print("Due chiavi uguali, non fatto nulla")
                                messages.info(request, '"{}" was assigned to two different points of interest!'.format(newPoi))
                                return redirect('/edit/tour/{}/points'.format(classid))
            except KeyError:
                pass
            return redirect('/Tour/{}'.format(classid))
    else:
        #poi_in_Tour = AArtTourTour.objects.filter(tour=classid).order_by('num')
        context = {
            'tour': Tour.objects.get(classid=classid),
            'poi': poi_in_Tour,
            'art': Art.objects.order_by('name_it'),
            'len': len(poi_in_Tour),
            'end': True if len(poi_in_Tour) < 15 else False
        }
        return render(request, 'editTourPoI.html', context)

def filterItemArt(request):
    category_db = ArtCategory.objects.order_by('classid')
    select = [None, True, True, True, True, True, True, True, True]
    if request.method == 'POST':

        category = ArtCategory.objects.none()
        category_t = AArtCategoryArtCategory.objects.none()
        state = DArtEStato.objects.none()
        art = Art.objects.none()
        cat = 0

        for c in range(1,len(category_db)+1):
            if 'categoria_{}'.format(c) in request.POST:
                cat += 1
                select[c] = True
                category |= ArtCategory.objects.filter(classid=str(c))
                category_t |= AArtCategoryArtCategory.objects.filter(category=str(c))
            else:
                select[c] = False

        if 'attivo' in request.POST:
            cat += 1
            select[7] = True
            state |= DArtEStato.objects.filter(code='01')
        else:
            select[7] = False

        if 'eliminato' in request.POST:
            cat += 1
            select[8] = True
            state |= DArtEStato.objects.filter(code='02')
        else:
            select[8] = False


        for c in category_t:
            new_art = Art.objects.filter(name_it=c.points).order_by('name_it')
            if select[8] and select[7]:
                    art |= new_art
            elif select[8]:
                art |= new_art.filter(state='02')
            elif select[7]:
                art |= new_art.filter(state='01')
        context = {
            'art': art,
            'category_t': category_t,
            'category': category,
            'category_db': category_db,
            'select' : select,
        }
    else:
        context = {
            'art': Art.objects.order_by('name_it'),
            'category_t': AArtCategoryArtCategory.objects,
            'category': ArtCategory.objects.order_by('classid'),
            'category_db': category_db,
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

def newArt(request):
    category = ArtCategory.objects.order_by('classid')

    if request.method == 'POST':
        #classid = request.POST['classid']

        with transaction.atomic():
            while True:
                try:
                    id = "".join(random.choices(string.digits, k=5))
                    Art.objects.get(classid=id)
                except:
                    art = Art(classid=id)
                    break
            print("codice: ", id)
            form = ArtForm(request.POST)

            while True:
                try:
                    id = "".join(random.choices(string.digits, k=5))
                    Location.objects.get(classid=id)
                except:
                    location = Location(classid=id, address=None, event=art.classid, num='1', geom=None)
                    break
            locationForm = LocationForm(request.POST)

            if form.is_valid() and locationForm.is_valid():
                art.descr_it = form.cleaned_data['descr_it']
                art.image_url = form.cleaned_data['image_url']
                art.name_it = form.cleaned_data['name_it']
                art.state = DArtEStato.objects.get(name='attivo')
                art.notes = form.cleaned_data['notes']
                art.open_time = form.cleaned_data['open_time']
                art.tickets = form.cleaned_data['tickets']
                #art.rss = form.cleaned_data['rss']
                #art.saving_vc = form.cleaned_data['saving_vc']
                art.vc = request.POST['vc']
                art.vc_id = form.cleaned_data['vc_id']

                saving_vc = form.cleaned_data['s_vc_perc']
                if saving_vc is None or saving_vc == 0:
                    art.saving_vc = 0.0
                else :
                    art.saving_vc = saving_vc / 100

                art.save()

                latitude = locationForm.cleaned_data['latitude']
                longitude = locationForm.cleaned_data['longitude']
                location.address = locationForm.cleaned_data['address']

                print(longitude, latitude)
                location.geom = Point(float(longitude), float(latitude))
                location.save()
            else:
                if 'open_time' in form.errors:
                    messages.info(request, "Field 'Open time' is too long!")
                    context = {
                        # 'lang': Lang.objects.get(active=True),
                        'form': ArtForm(),
                        'locationForm': LocationForm(),
                        'category': category,
                        'de_vc': DEVc.objects.order_by('code').reverse(),
                    }
                    return render(request, 'newArt.html', context)
                elif 'tickets' in form.errors:
                    messages.info(request, "Field 'Tickets' is too long!")
                    context = {
                        # 'lang': Lang.objects.get(active=True),
                        'form': ArtForm(),
                        'locationForm': LocationForm(),
                        'category': category,
                        'de_vc': DEVc.objects.order_by('code').reverse(),
                    }
                    return render(request, 'newArt.html', context)

            for c in range(1,len(category)+1):
                if 'categoria_{}'.format(c) in request.POST:
                    cat = ArtCategory.objects.get(classid=str(c))
                    category_t = AArtCategoryArtCategory(category=cat, points=art)
                    category_t.save()

        return redirect('/edit/translation/{}+{}'.format(art.classid,'en'))

    context = {
        #'lang': Lang.objects.get(active=True),
        'form': ArtForm(),
        'locationForm': LocationForm(),
        'category': category,
        'de_vc': DEVc.objects.order_by('code').reverse(),
    }
    return render(request, 'newArt.html',context)

def newTour(request):
    if request.method == 'POST':
        #classid = request.POST['classid']

        while True:
            try:
                id = "".join(random.choices(string.digits, k=5))
                Tour.objects.get(classid=id)
            except:
                tour = Tour(classid=id)
                break

        form = TourForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                tour.descr_it = form.cleaned_data['descr_it']
                tour.image_url = form.cleaned_data['image_url']
                tour.name_it = form.cleaned_data['name_it']
                tour.type = DTourETipoit.objects.get(name=form.cleaned_data['type'])
                #tour.kml_path = form.cleaned_data['kml_path']
                tour.duration = form.cleaned_data['duration']
                #tour.length = form.cleaned_data['length']

                tour.save()

        return redirect('/edit/tour/{}/points'.format(id))

    context = {
        'form' : TourForm()
    }
    return render(request, 'newTour.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('logIn')
        else:
            messages.info(request, "Passwords don't match!")
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
            messages.info(request, 'Authentication failed!')
            return redirect('logIn')
    else:
        return render(request, 'login.html')

def logOut(request):
    auth.logout(request)
    return redirect('/')

