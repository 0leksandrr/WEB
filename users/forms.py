from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class NewUserForm (UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'mail@gmail.com'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter username...'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter same password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

