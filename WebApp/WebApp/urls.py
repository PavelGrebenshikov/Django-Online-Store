from django.contrib import admin
from django.urls import path, include

# DEBUG
import debug_toolbar
from django.conf import settings
from django.urls import include, path


# MEDIA FILES
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('index/', include('main.urls')),
    path('', include('about.urls')),
    path('', include('register.urls')),
    path('', include('user.urls')),
    #path('', include('editprofile.urls')),
    path('', include('login.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()