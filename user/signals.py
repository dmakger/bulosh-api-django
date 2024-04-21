from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from chart.models import ChartProduct
from product.models import Product
from user.models import Profile


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
