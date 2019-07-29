from django import forms
from .models import Raccourci


class MiniURLForm(forms.ModelForm):
    class Meta:
        model = Raccourci
        fields = ('URLField','pseudo')
