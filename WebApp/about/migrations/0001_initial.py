# Generated by Django 3.1.1 on 2020-10-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EditAboutText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Изменение текста',
                'verbose_name_plural': 'Изменения текста',
                'db_table': '',
            },
        ),
    ]
