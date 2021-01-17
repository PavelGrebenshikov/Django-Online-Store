from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Slider, Edit, EditCenterText, VariousDetails, Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_product', 'discription', 'price', 'category', 'create_at', 'update_at', 'visible_point']
    list_display_links = ['id', 'name_product']
    search_fields = ['id', 'name_product', 'discription', 'visible_point']
    fields = ('name_product', 'discription', 'price', 'category', 'images',
              'get_images', 'visible_point')
    readonly_fields = ['create_at', 'update_at', 'get_images']

    def get_images(self, obj):
        if obj.images:
            return mark_safe(f'<img src="{obj.images.url}" width="75px">')
        else:
            return 'Фото не установлено'


class SliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'SliderImages']
    list_display_links = ['id', 'SliderImages']
    search_fields = ['id', 'SliderImages']


class EditAdmin(admin.ModelAdmin):
    list_display = ['id', 'EditHeadText', 'EditDisText', 'EditImages']
    list_display_links = ['id', 'EditHeadText']
    search_fields = ['id', 'EditHeadText']


class EditCenterTextAdmin(admin.ModelAdmin):
    list_display = ['id', 'WelcomeText', 'EditHeadText', 'EditCenterImage']
    list_display_links = ['id', 'WelcomeText']
    search_fields = ['id', 'WelcomeText']


class VariousDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'VariousImage']
    list_display_links = ['id', 'VariousImage']
    search_fields = ['id', 'VariousImage']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Edit, EditAdmin)
admin.site.register(EditCenterText, EditCenterTextAdmin)
admin.site.register(VariousDetails, VariousDetailsAdmin)


# it admin title and header

admin.site.site_title = 'Управление Онлайн-Магазином'
admin.site.site_header = 'Управлениe Онлайн-Магазином'