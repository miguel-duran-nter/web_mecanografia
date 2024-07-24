from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status, viewsets, permissions, generics
from meca.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from meca.forms import CustomUserChangeForm
from django.contrib.auth import login as auth_login, logout
from django.middleware.csrf import get_token

from .models import Scoreboard
from .serializers import LoginSerializer, ScoreboardSerializer, UserSerializer


class ScoreboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Scoreboard.objects.all()
    serializer_class = ScoreboardSerializer
    permission_classes = [permissions.AllowAny]


# @api_view(['POST'])
# @login_required
class SaveScoreView(generics.CreateAPIView):
    serializer_class = ScoreboardSerializer

    def post(self, request, *args, **kwargs):

        user_id = request.data.get("user_id")
        score = request.data.get("score")

        try:
            user = User.objects.get(id=user_id)
            scoreboard = Scoreboard.objects.create(user=user, score=score)
            scoreboard.save()
            return redirect("scoreboard")
        except User.DoesNotExist:
            return Response(
                {"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@login_required
def UserScoreboardView(request, user_id):
    scoreboard = Scoreboard.objects.filter(user_id=user_id).order_by("-score")

    context = {"scoreboard": scoreboard}

    return render(request, "scoreboard/scoreboard.html", context)


@login_required
def user_update_view(request, pk):
    user = get_object_or_404(User, id=pk)
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario actualizado correctamente")
            return redirect("user-update", pk=user.pk)
    else:
        form = CustomUserChangeForm(instance=user)

    return render(request, "registration/profile.html", {"form": form, "user": user})


class ScoreboardList(generics.ListAPIView):
    queryset = Scoreboard.objects.all()
    serializer_class = ScoreboardSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = permissions.IsAuthenticated


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data["user"]
            auth_login(request, user)
            request.session["logged"] = True

            return Response(
                {"detail": "Login successful", "redirect_url": f"/profile/{user.id}/"},
                status=status.HTTP_200_OK,
            )

        except ValidationError as e:
            return Response({"detail": e.detail}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )