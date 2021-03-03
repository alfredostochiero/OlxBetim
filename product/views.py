from django.shortcuts import render
from .models import Product,ProductImages


# Create your views here.

def product_list(request):
    productlist = Product.objects.all()

    context = {'productlist': productlist}

    return render(request, 'product/product_list.html', context)


def product_detail(request, product_slug):

    product = Product.objects.get(slug=product_slug)

    product_images = ProductImages.objects.filter(product=product)
    context = {'product': product, 'product_images': product_images}

    return render(request, 'product/product_detail.html', context)