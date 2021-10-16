from django.contrib import admin

from .models import *

class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'quantity', 'unit_price', 'purchase_date',)
    list_display_links = ('name',)
    list_editable = ('category', 'quantity', 'unit_price',)
    search_fields = ('name',)
    list_per_page = 8
    
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity_available')
    list_display_links = ('name',)
    list_editable = ('quantity_available',)
    search_fields = ('name',)
    list_per_page = 8


admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(Inventory, InventoryAdmin)

