from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/profile/', user, name='user'),
    path('user/edit_profile/', edit_profile_user, name='user_profile'),
]
