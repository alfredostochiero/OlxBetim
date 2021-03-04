from django.shortcuts import render
from .models import Product,ProductImages, Category
from django.core.paginator import Paginator
from django.db.models import Count

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    productlist = Product.objects.all()
    categorylist = Category.objects.annotate(total_products=Count('product'))

    if category_slug :
        category = Category.objects.get(slug=category_slug)
        productlist = productlist.filter(category=category)

    paginator = Paginator(productlist, 2)
    page = request.GET.get('page')
    productlist = paginator.get_page(page)

    context = {'productlist': productlist, 'categorylist': categorylist}
    return render(request, 'product/product_list.html', context)


def product_detail(request, product_slug):

    product = Product.objects.get(slug=product_slug)

    product_images = ProductImages.objects.filter(product=product)
    context = {'product': product, 'product_images': product_images}

    return render(request, 'product/product_detail.html', context)