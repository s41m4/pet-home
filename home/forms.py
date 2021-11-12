from django.db.models import fields
from django.forms import ModelForm
from django.shortcuts import redirect
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

class UserEditForm(forms.ModelForm):
    
    username = forms.CharField(
        label="Nom d'utilisateur", min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': "Nom d'utilisateur", 'id': 'form-username'}))

    first_name = forms.CharField(
        label='Prenom', min_length=2, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Prenom', 'id': 'form-firstname'}))

    last_name = forms.CharField(
        label='Nom', min_length=2, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Nom', 'id': 'form-lastname'}))

    email = forms.EmailField(
        max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class MyChangeFormPassword(PasswordChangeForm):
    pass

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['photo']


def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg