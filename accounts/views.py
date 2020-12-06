from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import (RegisterAccountForm)


# views
def register(request):
    # redirect if a user is already logged in
    if request.user.is_authenticated:
        return redirect('index')

    # handle posted form data
    if request.method == "POST":
        form = RegisterAccountForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = RegisterAccountForm()

    context = {'form': form}

    return render(request, 'accounts/register.html', context)
