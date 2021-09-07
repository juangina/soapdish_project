from django.contrib import admin

from .models import Conversation_Dialog, Conversation_Meta

class Conversation_MetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dialog_started', 'dialog_completed', 'created_date')
    list_display_links = ('id', 'name')
    list_editable = ('dialog_started','dialog_completed',)
    search_fields = ('name',)
    list_per_page = 3

class Conversation_DialogAdmin(admin.ModelAdmin):
    list_display = ('id', 'dialog', 'intent', 'created_date')
    list_display_links = ('id',)
    list_editable = ('dialog','intent',)
    search_fields = ('dialog',)
    list_per_page = 10

admin.site.register(Conversation_Meta, Conversation_MetaAdmin)
admin.site.register(Conversation_Dialog, Conversation_DialogAdmin)