from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Comment


admin.site.register(User, UserAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at') 
    search_fields = ('content', 'author__username')   

admin.site.register(Comment)