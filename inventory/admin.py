from django.contrib import admin

from .models import *

class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'quantity', 'unit', 'unit_price', 'price', 'purchase_date',)
    list_display_links = ('name',)
    list_editable = ('category', 'quantity', 'unit', 'unit_price', 'price',)
    search_fields = ('name',)
    list_per_page = 20
    
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity_available')
    list_display_links = ('name',)
    list_editable = ('quantity_available',)
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(Inventory, InventoryAdmin)

