from django.urls import path, include
from rest_framework.routers import SimpleRouter
# from .views.product_views import ProductListCreateAPIView
from .views import MenuListCreateAPIView, DishesListCreateAPIView

router = SimpleRouter()
# router.register(r'products', ProductListCreateAPIView)
router.register(r'menus', MenuListCreateAPIView, basename='menu')
router.register(r'dishes', DishesListCreateAPIView, basename='dish')

urlpatterns = [
    path('v1/', include(router.urls)),
]