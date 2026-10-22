from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import WorkExample
from .serializers import WorkExampleSerializer


class WorkExampleViewSet(viewsets.ModelViewSet):
    queryset = WorkExample.objects.all()
    serializer_class = WorkExampleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'
