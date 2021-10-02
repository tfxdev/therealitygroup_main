from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Floors)
admin.site.register(Beds)
admin.site.register(Baths)
admin.site.register(Property_features)


class PropertyImageAdmin(admin.StackedInline):
    model = PropertyImage


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageAdmin]

    class Meta:
        model = Property


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    pass
