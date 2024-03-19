from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views.product_views import ProductListCreateAPIView
from .views.menu_views import MenuListCreateAPIView

router = DefaultRouter()
# router.register(r'products', ProductListCreateAPIView)
router.register(r'menus', MenuListCreateAPIView, basename='menu')

urlpatterns = [
    path('v1/', include(router.urls)),
]