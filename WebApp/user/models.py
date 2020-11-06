from django.db import models
from django.contrib.auth.models import User, AbstractUser
#from django.db.models.signals import post_save
#from django.dispatch import receiver
from phone_field import PhoneField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneField(blank=True, help_text='Контактный номер телефона')
    birth_date = models.DateField('Дата рождения')
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
