from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'Index.html', {
        'title': "Jaguarete - Ecommerce",
        'topProducts': Product.objects.all()[:3],
        'products': Product.objects.all()
    })


def signin(request):
    return render(request, 'Sign_In.html', {})


def about(request):
    return render(request, 'About.html', {
        'title': "About"
    })


def details(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'user/products/Details.html', {
        'product': product
    })
<<<<<<< HEAD


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
        'id': id
    })


def delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('Home')
=======
>>>>>>> parent of 0e75ea2 (feat:Update and delete pages)
