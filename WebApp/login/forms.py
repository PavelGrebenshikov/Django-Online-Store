from django import forms


class LoginForm(forms.Form):
    user = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Логин'}), max_length=100)
    password = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Пароль'}), max_length=100)
