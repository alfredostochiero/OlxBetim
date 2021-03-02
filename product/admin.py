from django.contrib import admin
from .models import Product, Category, Brand, ProductImages

# Register your models here.




@admin.register(Product)
class ProductDisplay(admin.ModelAdmin):
    list_display = ('name', 'condition', 'brand'  ,'price')

@admin.register(Category)
class CategoryDisplay(admin.ModelAdmin):
    list_display = ('category_name',)

@admin.register(Brand)
class BrandDisplay(admin.ModelAdmin):
    list_display = ('brand_name','brand_nationality')

@admin.register(ProductImages)
class ProductImageDisplay(admin.ModelAdmin):
    pass
