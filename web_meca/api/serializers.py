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
        fields = ['username', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.mail)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('las_name', instance.las_name)
        instance.save()

        return instance