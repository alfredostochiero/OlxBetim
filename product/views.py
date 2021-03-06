from django.shortcuts import render
from .models import Product,ProductImages, Category
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404


# Create your views here.

def product_list(request, category_slug=None):
    category = None
    productlist = Product.objects.all()
    categorylist = Category.objects.annotate(total_products=Count('product'))
    user = ''
    if str(request.user) != 'AnonymousUser':
        user = request.user


    if category_slug :
        category = get_object_or_404(Category, slug=category_slug)
        productlist = productlist.filter(category=category)

    search_query = request.GET.get('q')
    # se for feito uma busca, essa irá filtrar se existe algum produto,descrição,marca, ou condição  do produto com essa palavra
    if search_query :
        productlist = productlist.filter(
            Q(name__icontains = search_query) |
            Q(description__icontains = search_query) |
            Q(brand__brand_name__icontains = search_query) |
            Q(condition__icontains= search_query) |
            Q(category__category_name__icontains = search_query)
        )



    paginator = Paginator(productlist, 2)
    page = request.GET.get('page')
    productlist = paginator.get_page(page)

    context = {'productlist': productlist, 'categorylist': categorylist, 'category': category, 'user': user}
    return render(request, 'product/product_list.html', context)


def product_detail(request, product_slug):

    user = ''
    if str(request.user) != 'AnonymousUser':
        user = request.user

    product = get_object_or_404(Product, slug=product_slug)

    product_images = ProductImages.objects.filter(product=product)
    context = {'product': product, 'product_images': product_images, 'user':user,}

    return render(request, 'product/product_detail.html', context,)