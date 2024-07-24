from rest_framework import serializers
from scoreboard.models import Scoreboard
from meca.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

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

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if not user:
                raise serializers.ValidationError('Incorrect credentials')
        else:
            raise serializers.ValidationError('Must include "username" and "password"')

        data['user'] = user
        return data
