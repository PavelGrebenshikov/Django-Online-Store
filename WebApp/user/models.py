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
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=128, blank=False, default='', verbose_name='Имя пользователя')
    surname = models.CharField(max_length=128, blank=False, default='', verbose_name='Фамилия пользователя')
    phone = PhoneField(blank=True, help_text='Контактный номер телефона', verbose_name='Номер телефона')
    pictures = models.ImageField(verbose_name='Аватар', default='images/users/Standard/avatar.jpg',
                                 upload_to='images/users/%Y/%m/%d')
    birth_date = models.DateField('Дата рождения', blank=False, default="1996-03-01", null=False)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь магазина'
        verbose_name_plural = 'Пользователи магазина'
