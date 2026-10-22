from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import User, MasterProfile
from .serializers import (
    UserSerializer,
    UserRegisterSerializer,
    MasterProfileCreateSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API для пользователей.
    - Регистрация нового пользователя
    - Получение списка пользователей (только для авторизованных)
    - Получение и обновление своего профиля
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'register':
            return UserRegisterSerializer
        if self.action == 'update_profile':
            return MasterProfileCreateSerializer
        return UserSerializer

    def get_queryset(self):
        # Авторизованный пользователь видит всех пользователей
        return User.objects.all()

    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        """Регистрация нового пользователя."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            UserSerializer(user).data,
            status=status.HTTP_201_CREATED
        )

    @action(detail=False, methods=['get', 'patch'], url_path='me')
    def me(self, request):
        """Получение и обновление своего профиля."""
        user = request.user
        if self.request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data)
        elif self.request.method == 'PATCH':
            # Обновляем данные пользователя
            user_serializer = UserSerializer(
                user, data=request.data, partial=True
            )
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()

            # Если есть данные для профиля мастера
            if 'master_profile' in request.data:
                profile, _ = MasterProfile.objects.get_or_create(user=user)
                profile_serializer = MasterProfileCreateSerializer(
                    profile, data=request.data['master_profile'], partial=True
                )
                profile_serializer.is_valid(raise_exception=True)
                profile_serializer.save()

            return Response(UserSerializer(user).data)

    @action(detail=False, methods=['get'], url_path='masters')
    def masters(self, request):
        """Получение списка всех мастеров."""
        masters = User.objects.filter(is_master=True)
        serializer = UserSerializer(masters, many=True)
        return Response(serializer.data)
