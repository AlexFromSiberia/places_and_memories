from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # include 'main' app urls
    path('', include('main.urls')),
    # include 'users' app urls
    path('users/', include('users.urls')),
]

