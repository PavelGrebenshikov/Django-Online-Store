from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField


@receiver(post_save, sender=User, dispatch_uid="create_profile")
def update_profile(sender, instance, **kwargs):
    if kwargs["created"]:
        Profile.objects.create(user=instance)


class Profile(models.Model):
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    phone = PhoneField(blank=True, help_text='Контактный номер телефона', verbose_name='Номер телефона')
    birth_date = models.DateField('Дата рождения', blank=True, default="1996-03-01", null=False)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь магазина'
        verbose_name_plural = 'Пользователи магазина'
