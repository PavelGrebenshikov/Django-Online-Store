from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
