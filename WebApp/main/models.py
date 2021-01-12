from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=128, blank=False)
    slug = models.SlugField(max_length=128, unique=True,
                            blank=True, default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-title']


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=None, verbose_name='Категория')
    name_product = models.TextField('Название продукта', max_length=128)
    discription = models.TextField('Описание')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    images = models.ImageField('Картинка', upload_to='images/Product/%Y/%m/%d')
    ToPut = models.BooleanField(default=True, verbose_name='Выставить на продажу')
    create_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name_product

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'
        ordering = ['-id']


class Slider(models.Model):
    SliderImages = models.ImageField(
        'Изображение слайдера', upload_to='images/slider/%Y/%m/%d')

    class Meta:
        db_table = 'slider'
        verbose_name = 'Изображение слайдера'
        verbose_name_plural = 'Изображения слайдера'


class Edit(models.Model):
    EditHeadText = models.TextField('Категории запчастей', max_length=128)
    EditDisText = models.TextField('Небольшой текст о запчастях')
    EditImages = models.ImageField(
        'Изображение для разных видов транспорта', upload_to='images/')
    UpdateTime = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.EditHeadText

    class Meta:
        db_table = 'parts'
        verbose_name = 'Об запчастях'
        verbose_name_plural = 'Об запчастях'


class EditCenterText(models.Model):
    WelcomeText = models.TextField('Гостьевой текст', max_length=128)
    EditHeadText = models.TextField(
        'Центральный текст', max_length=128)
    EditCenterImage = models.ImageField(
        'Главная центральная картинки', upload_to='images/ctrText/%Y/%m/%d')
    UpdateTimeCenterText = models.DateTimeField(auto_now=True, verbose_name='Дата обновления текста')

    def __str__(self):
        return self.WelcomeText

    class Meta:
        db_table = 'views'
        verbose_name = 'Центральный текст'
        verbose_name_plural = 'Центральные текста'


class VariousDetails(models.Model):
    VariousImage = models.ImageField('Различные детали', upload_to='images/Various/%Y/%m/%d')

    class Meta:
        db_table = 'various'
        verbose_name = 'Различные детали'
        verbose_name_plural = 'Различные детали'
