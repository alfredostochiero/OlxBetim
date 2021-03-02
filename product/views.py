from django.shortcuts import render
from .models import Product


# Create your views here.

def product_list(request):
    productlist = Product.objects.all()

    context = {'productlist':productlist}

    return render(request, 'product/product_list.html', context)

def product_detail(request,product_slug):

    product = Product.objects.get(slug=product_slug)
    context = {'product': product}

    return render(request, 'product/product_detail.html', context)