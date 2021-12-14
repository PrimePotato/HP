from django.shortcuts import render

# Create your views here.


# Load CSV

# Clear Data

# Grouped Data
from rest_framework import viewsets

from .serializers import CsvDataSerializer
from .models import CsvData


class CsvViewSet(viewsets.ModelViewSet):
    queryset = CsvData.objects.filter(price__gt=30e6)
    serializer_class = CsvDataSerializer
