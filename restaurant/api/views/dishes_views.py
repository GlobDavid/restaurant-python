from rest_framework import generics, viewsets
from restaurant.models import Dishes
from restaurant.api.serializers import DishesCreateSerializer, DishesGetAllSerializer, DishesGetByUUIDSerializer
class DishesListCreateAPIView(generics.ListCreateAPIView, viewsets.ViewSet):
    queryset = Dishes.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DishesCreateSerializer
        elif self.request.method == 'GET' and 'id' in self.request.query_params:
            return DishesGetByUUIDSerializer

        return DishesGetAllSerializer
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        uuid = self.request.query_params.get('id')
        if uuid:
            dish_serializer = DishesGetByUUIDSerializer()
            dish = dish_serializer.get_dish_by_uuid(uuid)
            queryset = Dishes.objects.filter(id_dish=dish.id_dish)
        return queryset