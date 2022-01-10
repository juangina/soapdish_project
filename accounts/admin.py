from django.contrib import admin
from .models import *

class PrimaryAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'address', 'city', 'state', 'zipcode', 'date_added', 'most_recent',)
    list_display_links = ('id', 'customer',)
    list_editable = ('most_recent',)
    search_fields = ('customer',)
    list_per_page = 50

admin.site.register(PrimaryAddress, PrimaryAddressAdmin)