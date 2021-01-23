from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Profile
from .forms import ProfileUserForm, UserNameEditFrom
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def edit_profile_user(request):
    if request.method == "POST":
        form = ProfileUserForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/profile/')
    else:
        form = ProfileUserForm()
    return render(request, 'user/edit_profile.html', context={"form": form})


def user(request):
    user = User.objects.get(id=request.user.id)
    add_profile = Profile.objects.get(id=request.user.profile.id)
    return render(request, 'user/user.html', {"user": user, "add_profile": add_profile})
