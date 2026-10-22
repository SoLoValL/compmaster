from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API для отзывов.
    - Чтение опубликованных отзывов — всем
    - Создание/редактирование/удаление — только авторизованным
    """
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Review.objects.all()
        return Review.objects.filter(is_published=True)

    def perform_create(self, serializer):
        # Если пользователь авторизован — сохраняем его как клиента
        if self.request.user.is_authenticated:
            serializer.save(customer=self.request.user)
        else:
            serializer.save()
