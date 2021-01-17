from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='accounts/register')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect('/accounts/login/')
        else:
            messages.error(request, 'Ошибка при регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
