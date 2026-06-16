from django.contrib import admin
from .models import Product, Category, Tag, Review

# Register remaining models without using decorator syntax that expects a ModelAdmin
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Review)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # This displays these specific database columns as rows in the admin list view
    list_display = ('id', 'name', 'price', 'category', 'quantity')
    
    # Adds a useful search bar to look up products quickly by name or category
    search_fields = ('name', 'category')
    
    # Adds a filtering sidebar on the right to segment items by category
    list_filter = ('category',)

