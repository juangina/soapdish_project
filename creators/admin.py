from django.contrib import admin

from .models import Creator

class CreatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date', 'is_mvc')
    list_display_links = ('id', 'name')
    list_editable = ('is_mvc',)
    search_fields = ('name',)
    list_per_page = 2


admin.site.register(Creator, CreatorAdmin)
