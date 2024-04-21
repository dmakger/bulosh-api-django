from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from metric.models import Category, AmountUnit, ParentAmountUnit


# Родительская единица измерения. (ВЕС, ОБЪЕМ, и т.д.)
class ParentAmountUnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


# Единица измерения. (Килограммы, граммы, литры)
class AmountUnitAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'shortname', 'parent', 'id']


# Категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


admin.site.register(ParentAmountUnit, ParentAmountUnitAdmin)
admin.site.register(AmountUnit, AmountUnitAdmin)
admin.site.register(Category, DraggableMPTTAdmin)
