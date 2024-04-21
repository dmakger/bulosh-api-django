from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


# ========{ ЕДИНИЦЫ ИЗМЕРЕНИЯ }========
# Родительская единица измерения. (ВЕС, ОБЪЕМ, и т.д.)
class ParentAmountUnit(models.Model):
    name = models.CharField('Название', max_length=128)

    class Meta:
        verbose_name = "Родительская единица измерения"
        verbose_name_plural = "Родительские единицы измерения"

    def __str__(self):
        return self.name


# Единица измерения. (Килограммы, граммы, литры)
class AmountUnit(models.Model):
    fullname = models.CharField('Полное название', max_length=64)
    shortname = models.CharField('Короткое название', max_length=16)
    parent = models.ForeignKey(ParentAmountUnit, on_delete=models.CASCADE, verbose_name='Родительская единица измерения',
                               help_text="Вес, объем, и т.д.")

    class Meta:
        verbose_name = "Единица измерения"
        verbose_name_plural = "Единицы измерения"

    def __str__(self):
        return self.fullname


# ========{ КАТЕГОРИИ }========
# Категории
class Category(MPTTModel):
    name = models.CharField('Название', max_length=128)
    parent = TreeForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

