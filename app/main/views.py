from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .models import Topic, Entry
# from .forms import TopicForm, EntryForm
from django.http import Http404


def index(request):
    """Welcome page"""
    return render(request, 'main/index.html')
