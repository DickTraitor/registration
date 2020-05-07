from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
    email=forms.EmailField(required=False)
    class Meta:
        model=User
        fields=['username','email']

   