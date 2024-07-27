from django.shortcuts import render
from .models import Product


# Create your views here.


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'online_shop/home.html', context)


def product_detail(request, id):
    product = Product.objects.get(pk=id)
    context = {
        'product': product,
    }
    return render(request, 'online_shop/detail.html', context)


