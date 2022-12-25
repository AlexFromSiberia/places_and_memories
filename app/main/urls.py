from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Places, Memories, MemoryUpdate, MemoryDelete, add_memory   #MemoryAdd

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    # the page with all places
    path('places/', Places.as_view(), name='places'),
    # # the page with info on specific place
    path('memories/<str:slug>/<int:pk>/', Memories.as_view(), name='memories'),

    # # the page to add new places
    # path('add_memory/', MemoryAdd.as_view(), name='add_memory'),
    path('add_memory/', add_memory, name='add_memory'),

    # Page for updating an entry.
    path('update_memory/<str:slug>/<int:pk>/', MemoryUpdate.as_view(), name='update_memory'),

    # Page for deleting an entry.
    path('delete_memory/<str:slug>/<int:pk>/', MemoryDelete.as_view(), name='delete_memory'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
