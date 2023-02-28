from django import forms
from .models import *


class RatsForm(forms.ModelForm):

    class Meta:
        model = Rats
        fields = ('id', 'name', 'description')

class MouseTrapForm(forms.ModelForm):
    class Meta:
        model = MouseTrap
        fields = ('id', 'image', 'rats', 'created_by')

class MouseTrap2Form(forms.ModelForm):
    class Meta:
        model = MouseTrap
        fields = ('id', 'image')