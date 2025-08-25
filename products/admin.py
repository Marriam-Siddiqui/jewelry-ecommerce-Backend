# products/admin.py
from django.contrib import admin
from .models import Category, Product, ProductImage, ProductReview

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'jewelry_type', 'in_stock', 'featured']
    list_filter = ['category', 'jewelry_type', 'in_stock', 'featured']
    search_fields = ['name', 'description']
    inlines = [ProductImageInline]

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'is_approved']
    list_filter = ['rating', 'is_approved']
    search_fields = ['product__name', 'user__email']