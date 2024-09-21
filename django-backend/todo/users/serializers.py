from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'telegram_user_id', 'user_id']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):
        if self.instance:
            return value
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with that username already exists.")
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
