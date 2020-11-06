from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('index/', include('main.urls')),
    path('', include('about.urls')),
    path('', include('register.urls')),
    path('', include('user.urls')),
    path('', include('editprofile.urls')),
    path('', include('login.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
