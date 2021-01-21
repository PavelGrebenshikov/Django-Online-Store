from django import forms
from django.contrib.auth.models import User
from .models import Profile


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'surname', 'phone', 'birth_date', 'pictures']


class UserNameEditFrom(forms.ModelForm):
    first_name = forms.CharField(max_length=11, label='Имя пользователя', widget=forms.TextInput())
    last_name = forms.CharField(max_length=11, label='Фамилия пользователя', widget=forms.TextInput())
    email = forms.EmailField(max_length=11, label='Электронная почта', widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
