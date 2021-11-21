from django.forms import ModelForm, TextInput
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import *


class ArtForm(ModelForm):
    s_vc_perc = forms.FloatField(min_value=0, max_value=100, required=False, widget=forms.NumberInput
                           (attrs={'placeholder': 'Percentuale sconto'}))

    class Meta:
        model = Art

        fields = ['name_it', 'descr_it', 'image_url', 'notes', 'open_time',
                  'tickets', 'vc', 'vc_id']

        widgets = {
            'name_it': forms.TextInput(attrs={'placeholder': 'Nome punto di interesse'}),
            'image_url': forms.TextInput(attrs={'placeholder': "Url dell'immagine"}),
            'vc_id': forms.TextInput(attrs={'placeholder': 'Identificativo per la verona card'}),
        }

        labels = {
            'name_it': _('Name'),
            'descr_it': _('Description'),
            'image_url': _('Image Url'),
            'vc': _('Verona Card')
        }
        help_texts = {

        }
        error_messages = {

        }

class ArtForm_Trad(ModelForm):
    class Meta:
        model = Art
        fields = ['name_it', 'descr_it', 'open_time', 'tickets',]
        labels = {
            'name_it': _('Name'),
            'descr_it': _('Description'),
        }

        widgets = {
            'name_it': forms.TextInput(attrs={'placeholder': 'Nome punto di interesse'}),
        }

class ArtForm_data(ModelForm):
    s_vc_perc = forms.FloatField( min_value=0, max_value=100)

    class Meta:
        model = Art
        fields = ['image_url', 'notes', 'open_time',
                  'tickets', 'vc', 'vc_id']
        labels = {
            'image_url': _('Image Url'),
            'vc': _('Verona Card')
        }

        widgets = {
            'image_url': forms.TextInput(attrs={'placeholder': "Url dell'immagine"}),
            'vc_id': forms.TextInput(attrs={'placeholder': 'Identificativo per la verona card'}),
        }

class TourForm(ModelForm):
    class Meta:
        model = Tour
        #fields = ['name_it', 'type', 'descr_it', 'image_url', 'kml_path', 'duration', 'length']
        fields = ['name_it', 'type', 'descr_it', 'image_url', 'duration']

        labels = {
            'name_it': _('Name'),
            'descr_it': _('Description'),
            'image_url': _('Image Url'),
        }

        widgets = {
            'name_it': forms.TextInput(attrs={'placeholder': 'Nome punto del tour'}),
            'image_url': forms.TextInput(attrs={'placeholder': "Url dell'immagine"}),
            'duration': forms.TextInput(attrs={'placeholder': 'Durata in ore'}),
        }

class LocationForm(forms.Form):
    latitude = forms.FloatField( min_value=-90, max_value=90, widget= forms.TextInput(attrs={'placeholder': 'Latitudine'}))
    longitude = forms.FloatField( min_value=-180, max_value=180, widget= forms.TextInput(attrs={'placeholder': 'Longitudine'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Indirizzo'}))