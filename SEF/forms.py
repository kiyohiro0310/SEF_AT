from django import forms
from SEF.models import pets

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = pets
        fields = ("message",)   # NOTE: the trailing comma is required