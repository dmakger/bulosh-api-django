from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ad.models import Poster
from ad.serializers import PosterSerializer


class PosterView(viewsets.ModelViewSet):
    serializer_class = PosterSerializer
    queryset = Poster.objects.all()
    permission_classes = [permissions.AllowAny]

    # Получение всех продуктов
    @action(methods=['get'], detail=False)
    def all(self, request, **kwargs):
        queryset = self.get_queryset().filter(is_visible=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
