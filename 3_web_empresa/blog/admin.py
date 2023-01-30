from django.contrib import admin
from .models import Category, Post
from django.urls import reverse
from django.utils.html import format_html, format_html_join


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'author_link', 'published', 'post_categories', 'post_categories_link')
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def author_link(self, obj):
        return format_html('<a href="{}">{}</a>', reverse('admin:auth_user_change', args=(obj.author.id,)), obj.author.username)

    author_link.short_description = 'Autor'

    def post_categories(self, obj):
        return ", ".join([cat.name for cat in obj.categories.all().order_by('name')])

    post_categories.short_description = 'Categorías'

    def post_categories_link(self, obj):
        # reverse('admin:{}_{}_change'.format(obj._meta.app_label, obj._meta.model_name), args=(child.pk,))
        return format_html_join(', ', '<a href="{}">{}</a>',
                                [(reverse(('admin:blog_category_change'), args=(cat.id,)), cat.name)
                                 for cat in obj.categories.all().order_by('name')]
                                )

    post_categories_link.short_description = 'Categorías'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
