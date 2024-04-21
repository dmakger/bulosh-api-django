from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from metric.models import AmountUnit, Category, ParentAmountUnit
from product.models import Product


# Родительская единица измерения. (ВЕС, ОБЪЕМ, и т.д.)
class ParentAmountUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentAmountUnit
        fields = '__all__'


# Единица измерения. (Килограммы, граммы, литры)
class AmountUnitSerializer(serializers.ModelSerializer):
    parent = ParentAmountUnitSerializer()

    class Meta:
        model = AmountUnit
        fields = '__all__'


# Категории
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


# Категории
class CategoryTreeSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'children']
