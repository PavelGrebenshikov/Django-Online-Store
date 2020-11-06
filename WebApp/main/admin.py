from django.contrib import admin
from .models import Product, Slider, Edit, EditCenterText, VariousDetails, Category

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Slider)
admin.site.register(Edit)
admin.site.register(EditCenterText)
admin.site.register(VariousDetails)
