from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price','digital','bar','stock', 'instock')
    list_display_links = ('id', 'name')
    list_editable = ('price','stock', 'instock')
    search_fields = ('name',)
    list_per_page = 50

admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)