from django.contrib import admin

from .models import Tag, Post, Comment

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ['title', 'published_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
