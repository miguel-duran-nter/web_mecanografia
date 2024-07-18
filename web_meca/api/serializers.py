from rest_framework import serializers
from scoreboard.models import Scoreboard
from meca.models import User

class ScoreboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scoreboard
        fields = ('id', 'user', 'score', 'created_at')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'last_login', 'date_joined']