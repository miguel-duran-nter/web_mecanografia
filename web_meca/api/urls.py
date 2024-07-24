from django.urls import path
# from rest_framework import routers
from api import views
# from meca.views import profile_view

# app_name = 'api'

urlpatterns = [
    path('save-score/', views.SaveScoreView.as_view(), name='save_score'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('scoreboard/', views.ScoreboardList.as_view(), name='scoreboard'),
    path('login/', views.LoginView.as_view()),
]