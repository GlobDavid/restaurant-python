from django.urls import path, include
from rest_framework import routers
from .views.product_views import ProductListCreateAPIView

"""
router = routers.DefaultRouter()
router.register(r'products', ProductListCreateAPIView)
"""
urlpatterns = [
    # path('v1/', include(router.urls)),
]