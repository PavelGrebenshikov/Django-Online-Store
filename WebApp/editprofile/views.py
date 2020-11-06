from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EditProfile
from django.contrib.auth.models import User

# Create your views here.


def edit_profile(request):
    if request.method == "POST":
        form = EditProfile(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            user_pictures = form.cleaned_data.get("user_pictures")
            email = form.cleaned_data.get("email")
            phone = form.cleaned_data.get("phone")

            defaults = {'first_name': first_name, 'last_name': last_name,
                        'user_pictures': user_pictures, 'email': email,
                        'phone': phone, }
            try:
                obj = User.objects.get(id=request.user.id)
                for key, value in defaults.items():
                    setattr(obj, key, value)
                obj.save()

                return HttpResponseRedirect('/accounts/profile/')
            except User.DoesNotExist:
                new_values = {'first_name': 'John', 'last_name': 'Lennon'}
                new_values.update(defaults)
                obj = User(**new_values)
                obj.save()
    else:
        form = EditProfile()
    return render(request, 'user/edit_profile.html', {'form': form})
