from dataclasses import fields
from pyexpat import model
from django import forms
from .models import userdata

class userForm(forms.ModelForm):
    class Meta:
        model=userdata
        fields='__all__'
