from django import forms


class EditProfile(forms.Form):
    first_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Имя'}), max_length=100)
    last_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Фамилия'}), max_length=100)
    user_pictures = forms.ImageField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Фотография'}), max_length=100)
    email = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Эл.почта'}), max_length=100)
    phone = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Телефон'}), max_length=100)
