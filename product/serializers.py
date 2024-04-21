from rest_framework import serializers

from metric.serializers import AmountUnitSerializer, CategorySerializer
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    amountUnit = serializers.SerializerMethodField()
    createdAt = serializers.SerializerMethodField()
    deletedAt = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'image',
            'category',
            'amount',
            'amountUnit',
            'createdAt',
            'deletedAt',
        ]

    def get_amountUnit(self, instance):
        return AmountUnitSerializer(instance.amount_unit).data

    def get_createdAt(self, instance):
        return instance.created_at

    def get_deletedAt(self, instance):
        return instance.deleted_at
