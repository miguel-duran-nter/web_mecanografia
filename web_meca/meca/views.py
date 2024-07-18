from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout, authenticate, login
from .forms import CustomUserCreationForm, CustomAuthenticationForm

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