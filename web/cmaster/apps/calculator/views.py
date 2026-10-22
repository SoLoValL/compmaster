from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import CalculatorCategory, CalculatorOption
from .serializers import CalculatorCategorySerializer, CalculatorOptionSerializer


class CalculatorCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Категории работ — только чтение."""
    queryset = CalculatorCategory.objects.filter(is_active=True)
    serializer_class = CalculatorCategorySerializer
    lookup_field = 'slug'


class CalculatorOptionViewSet(viewsets.ModelViewSet):
    """Опции — CRUD, но менять может только авторизованный."""
    queryset = CalculatorOption.objects.filter(is_active=True)
    serializer_class = CalculatorOptionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
