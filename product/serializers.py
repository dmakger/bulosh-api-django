from rest_framework import serializers

from metric.serializers import AmountUnitSerializer, CategorySerializer
from product.models import Product, Cart


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    amountUnit = serializers.SerializerMethodField()
    countAdded = serializers.SerializerMethodField()
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
            'countAdded',
            'createdAt',
            'deletedAt',
        ]

    def get_amountUnit(self, instance):
        return AmountUnitSerializer(instance.amount_unit).data

    def get_countAdded(self, instance):
        # print(instance.user)
        user = self.context.get('user')
        if user is None:
            return 0
        cart_qs = Cart.objects.filter(user=user, product=instance)
        if len(cart_qs) == 0:
            return 0
        return cart_qs[0].count

    def get_createdAt(self, instance):
        return instance.created_at

    def get_deletedAt(self, instance):
        return instance.deleted_at
