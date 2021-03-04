from django.shortcuts import render
from .models import Product,ProductImages, Category
from django.core.paginator import Paginator
from django.db.models import Count

# Create your views here.

def product_list(request):
    productlist = Product.objects.all()
    category_list = Category.objects.annotate(total_products=Count('product'))

    paginator = Paginator(productlist, 2)
    page = request.GET.get('page')
    productlist = paginator.get_page(page)

    context = {'productlist': productlist, 'category_list': category_list}
    return render(request, 'product/product_list.html', context)


def product_detail(request, product_slug):

    product = Product.objects.get(slug=product_slug)

    product_images = ProductImages.objects.filter(product=product)
    context = {'product': product, 'product_images': product_images}

    return render(request, 'product/product_detail.html', context)