from django import forms
from .models import signup_master


class signupForm(forms.ModelForm):
    class Meta:
        model=signup_master
        fields='__all__'