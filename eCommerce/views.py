from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'Index.html', {
        'title': "Jaguarete - Ecommerce",
        'topProducts': Product.objects.all()[:3],
        'products': Product.objects.all()
    })


def about(request):
    return render(request, 'About.html', {
        'title': "About"
    })


def details(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'user/products/Details.html', {
        'product': product
    })
