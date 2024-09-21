from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'views_counter')

