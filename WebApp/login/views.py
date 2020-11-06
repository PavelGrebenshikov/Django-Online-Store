from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
# Create your views here.


def Singup(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    else:
        form = LoginForm()
    return render(request, 'registration/register.html', {'form': form})
