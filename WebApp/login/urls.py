from django.urls import path, include
from . import views

urlpatterns = [
    path('registrations/login/', views.Singup, name='login'),
]
