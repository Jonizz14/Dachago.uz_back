from django.contrib import admin
from .models import Product, Blog


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'price', 'created_at')
    search_fields = ('title_ru', 'title_uz', 'title_en')
    list_filter = ('created_at', 'price')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'published_date')
    search_fields = ('title_ru', 'title_uz', 'title_en')
