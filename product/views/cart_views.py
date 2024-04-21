from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product, Cart
from product.serializers import ProductSerializer


class CartView(APIView):
    permission_classes = [IsAuthenticated]  # Только для аутентифицированных пользователей

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        count = request.data.get('count', 1)

        if product_id is None:
            return Response({'error': 'Необходимо указать продукт.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Продукт с указанным идентификатором не найден.'}, status=status.HTTP_404_NOT_FOUND)

        queryset = Cart.objects.filter(product=product, user=request.user.profile)
        if queryset.exists():
            cart_item = queryset.first()
        else:
            cart_item = Cart(user=request.user.profile, product=product, count=count)
        cart_item.count = count
        cart_item.save()
        if count <= 0:
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = ProductSerializer(cart_item.product, context={'user': request.user.profile})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
