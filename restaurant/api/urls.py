from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views.product_views import ProductListCreateAPIView
from .views import MenuListCreateAPIView, DishesListCreateAPIView

router = DefaultRouter()
# router.register(r'products', ProductListCreateAPIView)
router.register(r'menus', MenuListCreateAPIView, basename='menu')
router.register(r'dishes', DishesListCreateAPIView, basename='menu')

urlpatterns = [
    path('v1/', include(router.urls)),
]