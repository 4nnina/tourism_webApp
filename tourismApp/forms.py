from django.forms import ModelForm, TextInput
from .models import *

class ArtForm(ModelForm):
    class Meta:
        model = Art
        fields = ['name_it', 'descr_it','image_url','state','notes','open_time','tickets','rss','saving_vc','vc','vc_id']
"""
class ArtEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        art = kwargs.pop('art')
        super(ArtEditForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Art
        fields = ['name_it', 'descr_it', 'image_url', 'state', 'notes', 'open_time', 'tickets', 'rss', 'saving_vc', 'vc',
                  'vc_id']
                  
"""