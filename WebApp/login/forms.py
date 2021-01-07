from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    user = forms.CharField(label='Введите свой логин', widget=forms.TextInput(
        attrs={'placeholder': 'Логин'}))
    password = forms.CharField(label='Введите свой пароль', widget=forms.PasswordInput(
        attrs={'placeholder': 'Пароль'}))
