from django.contrib import admin

from user.models import Profile


# Профиль
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'id']


admin.site.register(Profile, ProfileAdmin)
