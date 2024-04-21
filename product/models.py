from django.db import models

from metric.models import Category, AmountUnit


# Продукт
from user.models import Profile


class Product(models.Model):
    name = models.CharField('Название', max_length=128)
    description = models.TextField('Описание')
    price = models.FloatField('Цена')
    image = models.ImageField(upload_to='media/product/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    amount = models.FloatField(verbose_name='Количество')
    amount_unit = models.ForeignKey(AmountUnit, on_delete=models.CASCADE, verbose_name='Единица измерения')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    deleted_at = models.DateTimeField('Дата удаления', null=True, blank=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


# Продукты добавленные во внутрь продукт
class ProductToAddedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='related_added_products',)
    added_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Добавленный продукт', related_name='related_products_added')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = "Продукты внутри продукта"
        verbose_name_plural = "Продукты внутри продукта"

    def __str__(self):
        return f"{self.product} <= {self.added_product}"


# Корзина
class Cart(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    count = models.IntegerField('Количество добавленных', default=1)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = "Продукты внутри продукта"
        verbose_name_plural = "Продукты внутри продукта"

    def __str__(self):
        return f"{self.user} - {self.product} [{self.created_at}]"
