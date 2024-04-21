from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views.product_views import AllProductView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    # Продукт
    path("all/", AllProductView.as_view({'get': 'all'})),
]
