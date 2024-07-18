from django.shortcuts import render, redirect
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions, generics
from meca.models import User
from .models import Scoreboard
from django.contrib.auth.decorators import login_required

class ScoreboardViewSet (viewsets.ReadOnlyModelViewSet):
    queryset = Scoreboard.objects.all()
    serializer_class = ScoreboardSerializer
    permission_classes = [permissions.AllowAny]

class UserViewSet (viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user