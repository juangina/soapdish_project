from django.contrib import admin

from .models import *

class DocumentsAdmin(admin.ModelAdmin):
  list_display = ('upload', 'uploaded_at',)
  list_display_links = ('upload',)
  search_fields = ('upload',)

admin.site.register(Document, DocumentsAdmin)
