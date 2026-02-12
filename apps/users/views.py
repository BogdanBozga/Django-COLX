from django.contrib.auth import logout
from django.shortcuts import render, redirect

from apps.users.forms import UserCreationForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('shop:home')

def login(request):
    return render(request, 'users/login.html')