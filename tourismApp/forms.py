from django.forms import ModelForm, TextInput
from django.utils.translation import ugettext_lazy as _
from .models import *

class ArtForm(ModelForm):
    #def __init__(self, *args, **kwargs):
    #    self.fields['tickets'].error_messages = {
    #        'max_length': 'Too long'}

    class Meta:
        model = Art
        fields = ['name_it', 'descr_it', 'image_url', 'notes', 'open_time',
                  'tickets', 'rss', 'saving_vc', 'vc', 'vc_id']
        labels = {
            'name_it': _('Name'),
            'descr_it': _('Description'),
            'image_url': _('Image Url'),
        }
        help_texts = {

        }
        error_messages = {
            #'tickets': {'max_length': _('Too long'),}
        }

class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = ['name_it', 'type', 'descr_it', 'image_url', 'kml_path', 'duration', 'length']
        labels = {
            'name_it': _('Name'),
            'descr_it': _('Description'),
            'image_url': _('Image Url'),
        }