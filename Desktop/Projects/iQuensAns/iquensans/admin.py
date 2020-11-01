from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Post, Comment


# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'first_name',)
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, AccountAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author','post','body', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('author','body')
