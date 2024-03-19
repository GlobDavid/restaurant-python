from rest_framework import serializers
from restaurant.models import Menu

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
        fields = ['title', 'description']
        
    def get_all_menus(self):
        menus = Menu.objects.all()
        return menus