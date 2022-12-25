from django.contrib import admin
from django.urls import path, include
# чтобы иметь доступ к переменным MEDIA_URL, MEDIA_ROOT
from django.conf import settings
# static module for MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # include 'main' app urls
    path('', include('main.urls')),
    # include 'users' app urls
    path('users/', include('users.urls')),
    # include django-allauth paths
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
