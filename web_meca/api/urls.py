from django.urls import path
from rest_framework import routers
from api import views

app_name = 'api'

# router = routers.DefaultRouter()
# router.register(r'Scoreboard', views.ScoreboardViewSet)
# # router.register(r'Scoreboard personal', views.UserScoreboardView)
# router.register(r'Users', views.UserViewSet)

urlpatterns = [
    path('save-score', views.SaveScoreView.as_view()),
] # + router.urls