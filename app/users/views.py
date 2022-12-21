from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Registration of a new user page"""
    if request.method != 'POST':
        # shows empty form
        form = UserCreationForm()
    else:
        # process filled form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('main:index')

    # shows empty or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
