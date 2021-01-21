from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'username', 'surname', 'phone', 'birth_date', 'reg_date']
    list_display_links = ['id', 'user', 'username', 'surname', 'birth_date', 'reg_date']
    search_fields = ['id', 'user', 'username', 'surname', 'birth_date', 'reg_date']


admin.site.register(Profile, ProfileUserAdmin)
