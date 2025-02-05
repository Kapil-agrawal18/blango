from django.contrib import admin
from blog.models import Tag, Post

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_a')

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)