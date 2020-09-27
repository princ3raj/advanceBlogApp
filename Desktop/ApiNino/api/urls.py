
from django.urls import path
from .views import NinoRoomsAPIView



urlpatterns = [
path('', NinoRoomsAPIView.as_view()),
]