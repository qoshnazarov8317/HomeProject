from django.urls import path
from .views import ListHouseAPIView, ListRoomAPIView, DetailHouseAPIView, DetailRoomAPIView

urlpatterns = [
    path('house/', ListHouseAPIView.as_view()),
    path('room/', ListRoomAPIView.as_view()),
    path('house/<int:pk>/', DetailHouseAPIView.as_view()),
    path('room/<int:pk>/', DetailRoomAPIView.as_view()),
]
