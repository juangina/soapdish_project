from django.contrib import admin

from .models import *



class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name','email',)
    list_display_links = ('id', 'user',)
    list_editable = ('name','email',)
    search_fields = ('name',)
    list_per_page = 50

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price','digital','bar','stock', 'instock',)
    list_display_links = ('id', 'name',)
    list_editable = ('price','stock', 'instock',)
    search_fields = ('name',)
    list_per_page = 50

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date_ordered','complete', 'transaction_id','shipping_cost', 'total_cost')
    list_display_links = ('id', 'customer', 'transaction_id',)
    list_editable = ('complete','shipping_cost', 'total_cost')
    search_fields = ('customer',)
    list_per_page = 50

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'order','quantity', 'date_added',)
    list_display_links = ('id', 'order',)
    list_editable = ('quantity',)
    search_fields = ('product','order',)
    list_per_page = 50

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order','address', 'city', 'state', 'zipcode', 'date_added',)
    list_display_links = ('id', 'customer', 'order',)
    list_editable = ('address',)
    search_fields = ('customer','order',)
    list_per_page = 50

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product','vote', 'created',)
    list_display_links = ('id', 'customer',)
    list_editable = ('vote',)
    search_fields = ('customer','product',)
    list_per_page = 50

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'discountType','discountActive', 'startDate', 'stopDate',)
    list_display_links = ('id', 'customer',)
    list_editable = ('discountType', 'discountActive',)
    search_fields = ('customer','discountType',)
    list_per_page = 50

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Discount, DiscountAdmin)