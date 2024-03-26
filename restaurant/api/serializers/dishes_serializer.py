from rest_framework import serializers
from restaurant.models import Dishes
# from . import MenusGetAllSerializer

class DishesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        fields = [ 'name', 'description', 'price', 'available']
        
    def create(self, validate_data):
        dish = Dishes.objects.create(**validate_data)
        return dish
    
    
class DishesGetAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        fields = ['id_dish', 'name', 'description', 'price', 'available']
        
    def get_all_menus(self):
        dish = Dishes.objects.all()
        return dish
    
    """
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        menu_representation = MenusGetAllSerializer(instance.id_menus).data
        return {**representation, 'menu': menu_representation}
        
        
        In this week, I was practicing the framework Django, using in one project, 
        and doing the mandotoring Java course in Globant University that have a one-hundred hours. 
        I have no blocks, just working on Django but my mentor helps me   
        
        """
        

class DishesGetByUUIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        fields = '__all__'

    def get_dish_by_uuid(self, uuid):
        try:
            dish = Dishes.objects.get(id_dish=uuid)
            return dish
        except Dishes.DoesNotExist:
            raise serializers.ValidationError('Dish not found')