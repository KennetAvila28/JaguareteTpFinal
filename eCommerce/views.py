from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy, resolve
from django.views.generic import CreateView, FormView, UpdateView, DeleteView
from .Form import ProductForm

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


def detailsmod(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'moderador/Details.html', {
        'product': product
    })


class ProductCreateView(CreateView):
    model = Product
    form = ProductForm
    fields = '__all__'

    def get_success_url(self):
        return reverse('Home')


def update(request, id):
    product = Product.objects.get(pk=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('Home')
    return render(request, 'moderador/Update.html', {
        'form': form,
        'id':id
    })


def delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('Home')
