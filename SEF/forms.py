from django import forms
from SEF.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("firstname","lastname","username","email","phone","password",)