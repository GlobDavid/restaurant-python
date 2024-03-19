from rest_framework import generics, mixins
from restaurant.models import Products
from restaurant.api.serializers import ProductCreateSerializer, ProductListAllSerializer
class ProductListCreateAPIView(): #mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Products.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateSerializer
        return ProductListAllSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)