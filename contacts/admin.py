from django.contrib import admin

from .models import Contact, Message

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bar', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'bar')
    list_per_page = 25

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient1', 'recipient2', 'name', 'email', 'subject', 'is_read',)
    list_display_links = ('id', 'sender',)
    search_fields = ('name', 'email',)
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
admin.site.register(Message, MessageAdmin)

