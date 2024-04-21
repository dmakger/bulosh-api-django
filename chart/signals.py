from django.db.models.signals import post_save
from django.dispatch import receiver

from chart.models import ChartProduct
from product.models import Product


@receiver(post_save, sender=Product)
def create_chart_product(sender, instance, created, **kwargs):
    if created:
        ChartProduct.objects.create(product=instance)
