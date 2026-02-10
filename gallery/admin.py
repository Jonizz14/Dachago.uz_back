from django.contrib import admin
from .models import Product, Blog, Contact


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'price', 'created_at')
    search_fields = ('title_ru', 'title_uz', 'title_en')
    list_filter = ('created_at', 'price')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'published_date')
    search_fields = ('title_ru', 'title_uz', 'title_en')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_at', 'is_read')
    search_fields = ('name', 'email', 'message')
    list_filter = ('is_read', 'created_at')
    readonly_fields = ('created_at',)
    ordering = ['-created_at']
