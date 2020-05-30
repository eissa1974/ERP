from django import forms
#from django.forms import ModelForm
from . import models
from django.contrib.auth.models import User


class UserForm2(forms.ModelForm):
    class Meta:
        model = User
        fields = [
        'username' , 'first_name' , 'last_name' , 'email'
        ]

#class ProfileForm(forms.modelform):
class ProfileForm2(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = [
        'headline','bio','img'
        ]
