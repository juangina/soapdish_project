from django.contrib import admin
from .models import *

class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'created_at', 'user_id','cover_image',)
    list_display_links = ('id', 'title',)
    list_editable = ('body','cover_image',)
    search_fields = ('title',)
    list_per_page = 50

admin.site.register(Posts, PostsAdmin)




