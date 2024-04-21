from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views.cart_views import CartView
from product.views.detail_product_views import ProductDetailView
from product.views.product_views import AllProductView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    # Продукт
    path("all/", AllProductView.as_view({'get': 'all'})),
    path('all/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/update/', CartView.as_view(), name='cart'),
]
