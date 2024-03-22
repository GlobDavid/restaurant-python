from django.test import SimpleTestCase
from django.urls import reverse, resolve
from restaurant.api.views import MenuListCreateAPIView, DishesListCreateAPIView

class TestUrls(SimpleTestCase):
    
    def test_menu_list_url_resolves(self):
        url = reverse('menu-list')
        print(url)
        resolved = resolve(url)
        print(resolved)
        print(resolved.func.cls)
        self.assertEqual(resolved.func.cls, MenuListCreateAPIView)
        
        
    def test_dishes_list_url_resolves(self):
        url = reverse('dish-list')
        resolved = resolve(url)
        self.assertEqual(resolved.func.cls, DishesListCreateAPIView)