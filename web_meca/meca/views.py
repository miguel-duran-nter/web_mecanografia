from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserChangeForm
from meca.models import User

def home(request):
    text = "This is some sample text for typing practice."
    palabrasOriginales = text.split(' ')

    context = {
        'palabrasOriginales': palabrasOriginales
    }
    return render(request, 'meca/home.html', context)

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
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def logout(request):
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