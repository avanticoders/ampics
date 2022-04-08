from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Account, Upload

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['caption', 'category', 'image']
        # exclude = ['account']

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'email', 'profile_pic']
        # exclude = ['user']

class Signin(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']