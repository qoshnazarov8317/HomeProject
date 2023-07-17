from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import House, Room
from .serializers import HouseSerializer, RoomSerializer
# Create your views here.

class ListHouseAPIView(ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class DetailHouseAPIView(RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    
class ListRoomAPIView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class DetailRoomAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer