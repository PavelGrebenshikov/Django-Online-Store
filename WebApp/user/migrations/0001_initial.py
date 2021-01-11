# Generated by Django 3.1.4 on 2021-01-11 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Контактный номер телефона', max_length=31, verbose_name='Номер телефона')),
                ('birth_date', models.DateField(blank=True, default='1996-03-01', verbose_name='Дата рождения')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('record', models.CharField(max_length=128)),
                ('user', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь магазина',
                'verbose_name_plural': 'Пользователи магазина',
            },
        ),
    ]
