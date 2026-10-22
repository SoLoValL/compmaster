from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import RepairRequest
from .serializers import RepairRequestCreateSerializer, RepairRequestSerializer


class RepairRequestViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    Создание заявки, просмотр списка и одной заявки.
    Редактирование/удаление — только через админку.
    """
    queryset = RepairRequest.objects.all()
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return RepairRequestCreateSerializer
        return RepairRequestSerializer
