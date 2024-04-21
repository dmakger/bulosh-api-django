from django.contrib import admin

from product.models import Product, ProductToAddedProduct, Cart


# Продукт
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'amount', 'amount_unit', 'created_at', 'deleted_at']


# Продукты добавленные во внутрь продукт
class ProductToAddedProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'added_product', 'created_at']


# Корзина
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'created_at']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductToAddedProduct, ProductToAddedProductAdmin)
admin.site.register(Cart, CartAdmin)
