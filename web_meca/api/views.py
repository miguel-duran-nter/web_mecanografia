from django.shortcuts import render, redirect, get_object_or_404
from .serializers import ScoreboardSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions, generics
from meca.models import User
from .models import Scoreboard
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from meca.forms import CustomUserChangeForm

class ScoreboardViewSet (viewsets.ReadOnlyModelViewSet):
    queryset = Scoreboard.objects.all()
    serializer_class = ScoreboardSerializer
    permission_classes = [permissions.AllowAny]

# @api_view(['POST'])
# @login_required
class SaveScoreView(generics.CreateAPIView):
    serializer_class = ScoreboardSerializer

    def post(self, request, *args, **kwargs):

        user_id = request.data.get('user_id')
        score = request.data.get('score')

        try:
            user = User.objects.get(id=user_id)
            scoreboard = Scoreboard.objects.create(
                user=user,
                score=score
            )
            scoreboard.save()
            return redirect('scoreboard')
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@login_required
def UserScoreboardView(request, user_id):
    scoreboard = Scoreboard.objects.filter(user_id=user_id).order_by('-score')

    context = {
        'scoreboard': scoreboard
    }

    return render(request, 'scoreboard/scoreboard.html', context)

@login_required
def user_update_view(request, pk):
    user = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado correctamente')
            return redirect('user-update', pk=user.pk)
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'registration/profile.html', {'form': form, 'user': user})