from chart.models import ChartProduct
from product.models import Product


def add_count_product_chart(product: Product):
    queryset = ChartProduct.objects.filter(product=product)
    if queryset.exists():
        product_chart: ChartProduct = queryset.first()
    else:
        product_chart: ChartProduct = ChartProduct.objects.create(product=product)
    product_chart.count_views += 1
    product_chart.save()