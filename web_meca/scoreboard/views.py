from django.shortcuts import render, redirect
from .models import Scoreboard
from django.contrib.auth.decorators import login_required
        
def scoreboard_view(request):
    scoreboard = Scoreboard.objects.all().order_by('-score')[:10]
    context = {
        'scoreboard': scoreboard
    }
    return render(request, 'scoreboard/scoreboard.html', context)