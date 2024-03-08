from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.
# We will write our endpoints here
# Endpoint -> a location on the web server we are going to

class RoomView(generics.ListAPIView):
    # Will return to us all of the different rooms
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


