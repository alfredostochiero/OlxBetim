from django.contrib import admin
from .models import Product,Category

# Register your models here.




@admin.register(Product)
class ProductDisplay(admin.ModelAdmin):
    list_display = ('name', 'condition', 'price')

@admin.register(Category)
class CategoryDisplay(admin.ModelAdmin):
    list_display = ('category_name',)

