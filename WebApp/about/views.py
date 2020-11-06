from django.shortcuts import render
from django.http import HttpRequest
from .models import AboutCompany
from django.views.generic import ListView

# Create your views here.


class AboutView(ListView):
    model = AboutCompany
    template_name = 'about/about.html'
    context_object_name = 'About'
