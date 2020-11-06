from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpRequest
from django.contrib.auth.models import User
# Create your views here.


def user(request):
    user = User.objects.get(id=request.user.id)
    return render(request, 'user/user.html', {'user': user})
