from django.contrib import admin

from .models import *

class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('name', 'purchase_date', 'distributer','category', 'quantity', 'unit', 'unit_price', 'price',)
    list_display_links = ('name',)
    list_editable = ('category', 'quantity', 'unit', 'unit_price', 'price', 'distributer',)
    search_fields = ('name', 'distributer')
    list_per_page = 10
    
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity_available')
    list_display_links = ('name',)
    list_editable = ('quantity_available',)
    search_fields = ('name',)
    list_per_page = 10


admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(Inventory, InventoryAdmin)

