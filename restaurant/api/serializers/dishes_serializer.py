from rest_framework import serializers
from restaurant.models import Dishes
from . import MenusGetAllSerializer

class DishesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        fields = ['id_menu', 'name', 'description', 'price', 'available']
        
    def create(self, validate_data):
        dish = Dishes.objects.create(**validate_data)
        return dish
    
    
class DishesGetAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        fields = ['name', 'description', 'price', 'available']
        
    def get_all_menus(self):
        dish = Dishes.objects.all()
        return dish
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        menu_representation = MenusGetAllSerializer(instance.id_menu).data
        return {**representation, 'menu': menu_representation}