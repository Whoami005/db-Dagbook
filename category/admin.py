from django.contrib import admin

from category.models import Geolocation, Lifetime, Genre


class GeolocationModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)


class LifetimeModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)


class GenreModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)


admin.site.register(Geolocation, GeolocationModelAdmin)
admin.site.register(Lifetime, LifetimeModelAdmin)
admin.site.register(Genre, GenreModelAdmin)
