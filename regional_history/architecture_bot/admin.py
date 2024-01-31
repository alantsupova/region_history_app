from django.contrib import admin
from .models import Places, Routes


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'description', 'coordinate_x',
                    'coordinate_y')


@admin.register(Routes)
class RoutesAdmin(admin.ModelAdmin):
    list_display = ('title', 'time')
    filter_horizontal = ('places', )
