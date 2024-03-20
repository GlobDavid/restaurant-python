from rest_framework import generics, viewsets
from restaurant.models import Dishes
from restaurant.api.serializers import DishesCreateSerializer, DishesGetAllSerializer
class DishesListCreateAPIView(generics.ListCreateAPIView, viewsets.ViewSet):
    queryset = Dishes.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DishesCreateSerializer
        return DishesGetAllSerializer