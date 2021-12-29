from django.contrib import admin

from .models import Bar

class BarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'recipe','nutrients','exfolients','price', 'batch_code','is_cured')
    list_display_links = ('id', 'name')
    list_editable = ('nutrients','exfolients','is_cured',)
    search_fields = ('name',)
    list_per_page = 50


admin.site.register(Bar, BarsAdmin)
