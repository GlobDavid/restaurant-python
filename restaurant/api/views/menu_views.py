from rest_framework import generics, viewsets
from restaurant.models import Menu
from restaurant.api.serializers import MenuCreateSerializer, MenusGetAllSerializer, MenuGetByUUIDSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(manual_parameters=[openapi.Parameter('id', openapi.IN_QUERY, description='UUID parameter', type=openapi.TYPE_STRING)])      
class MenuListCreateAPIView(generics.ListCreateAPIView, viewsets.ViewSet):
    queryset = Menu.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MenuCreateSerializer
        elif self.request.method == 'GET' and 'id' in self.request.query_params:
            return MenuGetByUUIDSerializer
        else:
            return MenusGetAllSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        uuid = self.request.query_params.get('id')
        if uuid:
            menu_serializer = MenuGetByUUIDSerializer()
            menu = menu_serializer.get_menu_by_uuid(uuid)
            queryset = Menu.objects.filter(id_menu=menu.id_menu)
        return queryset