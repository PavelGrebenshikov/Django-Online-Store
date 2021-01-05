from django.db import models

# Create your models here.


class AboutCompany(models.Model):
    name = models.CharField('Имя сотрудника', max_length=128, blank=False)
    position = models.CharField(
        'Должность сотрудника', max_length=128, blank=False)
    discription = models.CharField(
        'Описание сотрудника', max_length=128, blank=False)
    images = models.ImageField('Фотография сотрудника', upload_to='images/')

    def __str__(self):
        return self.position

    class Meta():
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'
