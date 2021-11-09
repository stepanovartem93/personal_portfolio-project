from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'updated')
    list_filter= ('created', 'publish')
    search_fields  = ('title', )
    prepopulated_fields = {'slug': ('title',)} #автоматически формирует краткий заголовок
    date_hierarchy = 'publish'
    ordering = ('publish', )