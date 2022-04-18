from django.contrib import admin
from django.utils.safestring import mark_safe

from authors.models import Authors, Books


class AuthorsModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "nickname",
        "get_html_photo",
        "biography",
        "years_of_life",
        "nationality",
        "geolocation",
        "lifetime",
    )
    list_display_links = ("nickname", "name", "get_html_photo",)
    list_filter = ("geolocation__name", "lifetime__name", "nationality",)
    search_fields = ("name", "nickname",)
    fields = (
        "name",
        "nickname",
        "photo",
        "get_html_photo",
        "biography",
        "years_of_life",
        "nationality",
        "geolocation",
        "lifetime",
    )
    readonly_fields = ("get_html_photo",)
    save_on_top = True

    def get_html_photo(self, objects):
        if objects.photo:
            return mark_safe(f"<img src='{objects.photo.url}' width=50>")
    
    get_html_photo.short_description = "Фото"


class BooksModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "get_html_photo",
        "short_description",
        "book_translator",
        "file_book",
        "publisher_name",
        "city_of_publication",
        "year_of_publishing",
        "get_authors",
        "genre"
    )
    list_display_links = ("name", "get_html_photo",)
    list_filter = ("authors__name", "genre__name", "city_of_publication", "year_of_publishing", "publisher_name",)
    search_fields = ("name", "authors__name",)
    fields = (
        "name",
        "photo",
        "get_html_photo",
        "short_description",
        "book_translator",
        "file_book",
        "publisher_name",
        "city_of_publication",
        "year_of_publishing",
        "authors",
        "genre"
    )
    readonly_fields = ("get_html_photo",)
    save_on_top = True

    def get_html_photo(self, objects):
        if objects.photo:
            return mark_safe(f"<img src='{objects.photo.url}' width=50>")

    get_html_photo.short_description = "Картинка"

    def get_authors(self, obj):
        if obj.authors:
            return "\n".join([p.name for p in obj.authors.all()])

    get_authors.short_description = "Авторы"


admin.site.register(Authors, AuthorsModelAdmin)
admin.site.register(Books, BooksModelAdmin)
