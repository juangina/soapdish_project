from django.contrib import admin

from .models import Bar

class BarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'recipe', 'price', 'batch_code','is_cured')
    list_display_links = ('id', 'name')
    list_editable = ('is_cured',)
    search_fields = ('name',)
    list_per_page = 3


#admin.site.register(Bars, BarsAdmin)
admin.site.register(Bar, BarsAdmin)
