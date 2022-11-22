from django import forms
from .models import userSignup,mynotes

class usersignupForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'

class notesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields='__all__'
    
class updateForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields=['firstname','lastname','username','password','city','state','mobile']