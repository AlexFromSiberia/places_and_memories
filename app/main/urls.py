from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Places, Memories, MemoryUpdate

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    # the page with all places
    path('plases/', Places.as_view(), name='places'),
    # # the page with info on specific place
    path('memories/<str:slug>/', Memories.as_view(), name='memories'),

    # # the page to add new places
    # path('new_place/', views.new_place, name='new_place'),

    # Page for editing an entry.
    path('update_memory/<str:slug>/', MemoryUpdate.as_view(), name='update_memory'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
