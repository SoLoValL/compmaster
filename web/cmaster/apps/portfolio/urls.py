from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkExampleViewSet

router = DefaultRouter()
router.register(r'', WorkExampleViewSet, basename='work-example')

urlpatterns = [
    path('', include(router.urls)),
]
