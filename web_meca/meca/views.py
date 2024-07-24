from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token

from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserChangeForm
from .models import User

def home(request):
    is_logged = request.session.get('logged', False)
    return render(request, 'meca/home.html', {'is_logged': is_logged})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    csrf_token = get_token(request)
    response = render(request, 'registration/login1.html')
    response.set_cookie('csrftoken', csrf_token)
    return response

def logout(request):
    request.session['logged'] = False
    auth_logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    return redirect('user-update', pk=request.user.pk)

@login_required
def user_update_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'user_update.html', {'form': form})