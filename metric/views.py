from django.db.models import QuerySet
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from metric.models import Category
from metric.serializers import CategoryTreeSerializer


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategoryTreeSerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]

    # Получение всех продуктов
    @action(methods=['get'], detail=False)
    def all(self, request, **kwargs):
        categories: QuerySet[Category] = self.queryset.filter(parent=None)
        serializer_data = self.serializer_class(categories, many=True).data
        return Response(serializer_data, status=status.HTTP_200_OK)
