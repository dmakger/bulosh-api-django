from rest_framework import permissions, generics

from product.models import Product
from product.serializers import ProductDetailSerializer


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()  # Используем модель Product
    permission_classes = [permissions.AllowAny]

    # Получение всех продуктов
    def get_serializer_context(self):
        context = super().get_serializer_context()
        user = None
        if self.request.user.is_authenticated:
            user = self.request.user.profile
        context['user'] = user
        return context
