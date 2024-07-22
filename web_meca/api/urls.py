from django.urls import path
from rest_framework import routers
from api import views
from meca.views import profile_view

app_name = 'api'

urlpatterns = [
    path('save-score/', views.SaveScoreView.as_view(), name='save_score'),
    path('users/<int:pk>/update/', views.user_update_view, name='user-update'),
    path('profile/', profile_view, name='profile'),
] # + router.urls