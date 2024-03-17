import uuid
from rest_framework import serializers
from restaurant.models import Product
from restaurant.enums import CategoryEnum

# CREATE PRODUCT
class ProductCreateSerializer( serializers.ModelSerializer ):
    category = serializers.ChoiceField(choices=[(choice.value, choice.value) for choice in CategoryEnum])
    class Meta:
        model = Product
        fields = ['uuid', 'fantasyName', 'category', 'description', 'price', 'available']

    def create(self, validated_data):
        validated_data['uuid'] = uuid.uuid4().bytes
        product = Product.objects.create(**validated_data)
        return product
    

# LIST ALL PRODUCTS
class ProductListAllSerializer( serializers.ModelSerializer ):
    
    uuid = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_uuid(self, obj):
        return str(uuid.UUID(bytes=obj.uuid))

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['uuid'] = self.get_uuid(instance)
        return representation