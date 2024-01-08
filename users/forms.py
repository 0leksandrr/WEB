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

    # def clean_email(self):
    #     # Перевірка унікальності електронної пошти при реєстрації
    #     email = self.cleaned_data.get('email')
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError('Ця електронна пошта вже зареєстрована. Виберіть іншу.')
    #     return email