from django.shortcuts import render, get_object_or_404
from django.http import request, HttpResponseRedirect
from django.views.generic import ListView, CreateView
from .models import Profile
from .forms import ProfileUserForm, UserNameEditFrom
from django.contrib.auth.models import User


def edit_user_name(request):
    if request.method == "POST":
        form_name = UserNameEditFrom(data=request.POST, instance=request.user)
        if form_name.is_valid():
            form_name.save()
            return HttpResponseRedirect('/accounts/profile/')
    else:
        form_name = UserNameEditFrom()
    return render(request, 'user/edit_name_user.html', context={"form_name": form_name})


def edit_profile_user(request):
    if request.method == "POST":
        form = ProfileUserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/profile/')
    else:
        form = ProfileUserForm()
    return render(request, 'user/edit_add_profile.html', context={"form": form})


class EditProfile(ListView):
    model = User
    template_name = 'user/edit_profile.html'


def user(request):
    user = User.objects.get(id=request.user.id)
    add_profile = Profile.objects.get(id=request.user.id)
    return render(request, 'user/user.html', {"user": user, "add_profile": add_profile})
