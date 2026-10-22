from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CalculatorCategoryViewSet, CalculatorOptionViewSet

router = DefaultRouter()
router.register(r'categories', CalculatorCategoryViewSet, basename='category')
router.register(r'options', CalculatorOptionViewSet, basename='option')

urlpatterns = [
    path('', include(router.urls)),
]
