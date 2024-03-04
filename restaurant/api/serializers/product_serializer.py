from rest_framework import serializers
from restaurant.models import Product

# CREATE PRODUCT
class productCreateSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Product
        field = "__all__"

    def create( self, validate_data ):
        product = Product.objects.create(
            fantasyName = validate_data['fantasyName'],
            category = validate_data['category'],
            description = validate_data['description'],
            price = validate_data['price'],
            available = validate_data['available'],
        )

        return product