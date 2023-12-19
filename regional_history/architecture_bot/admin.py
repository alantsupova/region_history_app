from django.contrib import admin
from .models import Places, Routes


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ('title', 'address')


@admin.register(Routes)
class RoutesAdmin(admin.ModelAdmin):
    list_display = ('title', )
