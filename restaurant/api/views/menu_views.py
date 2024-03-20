from rest_framework import generics, viewsets
from restaurant.models import Menu
from restaurant.api.serializers import MenuCreateSerializer, MenusGetAllSerializer
class MenuListCreateAPIView(generics.ListCreateAPIView, viewsets.ViewSet):
    queryset = Menu.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MenuCreateSerializer
        return MenusGetAllSerializer