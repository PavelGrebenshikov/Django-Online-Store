from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect('/index/')
        else:
            messages.error(request, 'Ошибка при регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
