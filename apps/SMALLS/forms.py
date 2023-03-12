from django import forms
from .models import *


class SMALLSForm(forms.ModelForm):

    class Meta:
        model = SMALLS
        fields = ('_id', 'Latitude','Longitude')