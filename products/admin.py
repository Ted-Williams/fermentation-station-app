from django.contrib import admin
from .models import Product, Category



class ProductAdmin (admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('rating',)

    
class CategoryAdmin (admin.ModelAdmin):
    list_dipslay = (
        'friendly_name',
        'name',
    )

 

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
