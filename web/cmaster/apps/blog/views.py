from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API для статей блога.
    - Чтение доступно всем
    - Создание/редактирование/удаление — только авторизованным
    """
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Post.objects.filter(is_published=True)
        # Если запрошен конкретный пост по slug — даже не опубликованный
        slug = self.kwargs.get('slug')
        if slug:
            return Post.objects.filter(slug=slug)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
