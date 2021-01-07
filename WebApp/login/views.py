from django.contrib.auth.models import User
from .forms import LoginForm
from django.http import request, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout
# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = LoginForm.get_user()
            login(request, user)
            return HttpResponseRedirect('/index/')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', context={"form": form})