# Generated by Django 4.1 on 2024-04-21 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_cart_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзина'},
        ),
    ]