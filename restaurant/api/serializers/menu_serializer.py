from rest_framework import serializers
# from restaurant.api.serializers import DishesGetAllSerializer
from restaurant.models import Menu, Dishes


class MenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['title', 'description']
        
    def create(self, validate_data):
        menu = Menu.objects.create(**validate_data)
        return menu
    
    
class MenusGetAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id_menu','title', 'description']
        
    def get_all_menus(self):
        menus = Menu.objects.all()
        return menus
    

class DishesGetAllSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Dishes
        fields = ['id_dish', 'name', 'description', 'price', 'available']


from .dishes_serializer import DishesGetAllSerializer  # Mueve la importación aquí

class MenuGetByUUIDSerializer(serializers.ModelSerializer):
    dishes = DishesGetAllSerializer(many=True, read_only=True, source='menu')

    class Meta:
        model = Menu
        fields = '__all__'

    def get_menu_by_uuid(self, uuid):
        try:
            menu = Menu.objects.get(id_menu=uuid)
            return menu
        except Menu.DoesNotExist:
            raise serializers.ValidationError('Menu not found')

    def to_representation(self, instance):
        representation = super().to_representation(instance) # Obtener la representación original
        menu_representation = representation.copy() # Copiamos la representación original
        menu_representation.pop('dishes') # Eliminar el campo 'dishes'
        menu_representation['dishes'] = representation['dishes'] # Agregamos nuevamente el campo 'dishes' al final
        return menu_representation