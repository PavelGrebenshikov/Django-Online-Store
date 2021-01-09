from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/profile/', user, name='user'),
    path('user/edit_profile/', EditProfile.as_view(), name='user_profile'),
    path('user/edit_name_user/', edit_user_name, name='user_edit_name'),
    path('user/edit_add_profile/', edit_profile_user, name='user_edit_profile')
]
