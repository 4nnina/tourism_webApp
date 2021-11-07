from django.forms import ModelForm, TextInput
from django.utils.translation import ugettext_lazy as _
from .models import *

class MyForm(ModelForm):
    OPTIONS = ()

class ArtForm(ModelForm):

    class Meta:
        model = Art
        fields = ['name_it', 'descr_it', 'image_url', 'notes', 'open_time',
                  'tickets', 'saving_vc', 'vc', 'vc_id']
        labels = {
            'name_it': _('Name'),
            'descr_it': _('Description'),
            'image_url': _('Image Url'),
            'vc': _('Verona Card')
        }
        help_texts = {

        }
        error_messages = {
            #'tickets': {'max_length': _('Too long'),}
        }

class ArtForm_Name_Descr(ModelForm):

    class Meta:
        model = Art
        fields = ['name_it', 'descr_it',]
        labels = {
            'name_it': _('Name'),
            'descr_it': _('Description'),
        }

class ArtForm_data(ModelForm):

    class Meta:
        model = Art
        fields = ['image_url', 'notes', 'open_time',
                  'tickets', 'saving_vc', 'vc', 'vc_id']
        labels = {
            'image_url': _('Image Url'),
            'vc': _('Verona Card')
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