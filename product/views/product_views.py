from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from product.filter import ProductFilter
from product.models import Product
from service.pagination import CustomPagination
from product.serializers import ProductSerializer


class AllProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()  # Используем модель Product
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['name', 'price']
    ordering = ['name']
    pagination_class = CustomPagination

    # Получение всех продуктов
    @action(methods=['get'], detail=False)
    def all(self, request, **kwargs):
        queryset: QuerySet[Product] = self.filter_queryset(self.get_queryset())  # Применяем фильтры
        count_views_sort = request.query_params.get('popularity')
        if count_views_sort:
            queryset = queryset.order_by('-chartproduct__count_views')

        user = None
        if request.user.is_authenticated:
            user = request.user.profile

        # Только добавленные товары в корзину
        only_added = request.query_params.get('only_added')
        if only_added:
            if user is None:
                queryset = Product.objects.none()
            queryset = queryset.filter(cart__user=user)

        page = self.paginate_queryset(queryset)  # Применяем пагинацию
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={"user": user})
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True, context={"user": user})
        return Response(serializer.data)
