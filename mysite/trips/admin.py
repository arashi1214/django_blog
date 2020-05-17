from django.contrib import admin
from .models import Post, Img

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_date', 'published_date', 'author_id')
    # list_filter = ('created_date',)
    # search_fields = ('title',)
    # ordering = ('text',)

admin.site.register(Post, PostAdmin)
admin.site.register(Img)
admin.site.site_url = 'http://127.0.0.1:8000/home'