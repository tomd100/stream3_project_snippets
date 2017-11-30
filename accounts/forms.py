from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserLoginForm(forms.Form):
    username = forms.CharField();
    password = forms.CharField(widget=forms.PasswordInput);