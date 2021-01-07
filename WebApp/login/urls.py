from django.urls import path, include
from .views import *

urlpatterns = [
    path('registrations/login/', user_login, name='login'),
]
