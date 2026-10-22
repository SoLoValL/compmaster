from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, MasterProfile


class MasterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterProfile
        fields = ['photo', 'bio', 'skills', 'rating', 'is_available']
        read_only_fields = ['rating']


class UserSerializer(serializers.ModelSerializer):
    master_profile = MasterProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
                  'is_master', 'phone', 'master_profile']
        read_only_fields = ['id']


class UserRegisterSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя."""
    password = serializers.CharField(write_only=True, required=True,
                                     validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm',
                  'first_name', 'last_name', 'phone']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError(
                {"password": "Пароли не совпадают."}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class MasterProfileCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания/обновления профиля мастера."""
    class Meta:
        model = MasterProfile
        fields = ['photo', 'bio', 'skills', 'is_available']
