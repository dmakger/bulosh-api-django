from django.contrib import admin

from ad.models import Poster


# Постеры
class PosterAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'id']


admin.site.register(Poster, PosterAdmin)
