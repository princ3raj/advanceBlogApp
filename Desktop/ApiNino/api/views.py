from django.shortcuts import render

from rest_framework import generics
from ninorooms.models import NinoRooms
from .serializers import NinoRoomsSerializer

# Create your views here.

class NinoRoomsAPIView(generics.ListAPIView):
    queryset=NinoRooms.objects.all()
    serializer_class=NinoRoomsSerializer

