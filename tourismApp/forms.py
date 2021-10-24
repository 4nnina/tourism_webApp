from django.forms import ModelForm, TextInput
from .models import *

class ArtForm(ModelForm):
    class Meta:
        model = Art
        fields = ['name_it', 'descr_it','image_url','notes','open_time','tickets','rss','saving_vc','vc','vc_id']