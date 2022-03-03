from django.contrib import admin

from .models import Bar

class BarsAdmin(admin.ModelAdmin):
    list_display = ('batch_code', 'for_sale', 'name', 'recipe','fragrance', 'nutrients','exfolients','clays', 'price', 'is_cured',)
    list_display_links = ('name',)
    list_editable = ('nutrients','exfolients', 'clays', 'is_cured','for_sale',)
    search_fields = ('name',)
    list_per_page = 50


admin.site.register(Bar, BarsAdmin)
