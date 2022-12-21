from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    # the page with all places
    path('plases/', views.topics, name='places'),
    # the page with info on specific place
    path('place/<str:slug>/', views.topic, name='place'),
    # the page to add new places
    path('new_place/', views.new_place, name='new_place'),
    # the page to add new memories
    path('new_memory/<str:slug>/', views.new_memory, name='new_memory'),
    # Page for editing an entry.
    path('edit_memory/<str:slug>/', views.edit_memory, name='edit_memory'),

]