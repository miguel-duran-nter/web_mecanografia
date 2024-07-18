from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import scoreboard_view
from api import views

# router = DefaultRouter()
# router.register(r'scoreboard', views.ScoreboardViewSet)

urlpatterns = [
    path('', scoreboard_view, name='scoreboard'),
    path('personal/<int:user_id>/', views.UserScoreboardView, name='user_scoreboard'),
    path('save-score/', views.SaveScoreView.as_view(), name='save_score'),
    # path('scoreboard/<int:user_id>/', views.UserScoreboardView, name='user_scoreboard'),
]