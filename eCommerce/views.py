from django.contrib.auth import authenticate, login, REDIRECT_FIELD_NAME, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, FormView
from .Form import ProductForm, SignUpForm, SignInForm

from .models import Product, Cart, Category


def index(request):
    queryset = request.GET.get('searchText')
    if queryset:
        return render(request, 'user/products/Filter.html', {'products': filter(queryset),
                                                             'categories': Category.objects.all(),
                                                             'searchText': queryset})
    else:
        return render(request, 'Index.html', {
            'title': "Jaguarete - Ecommerce",
            'topProducts': Product.objects.all()[:3],
            'products': Product.objects.all()[3:10],
            'user': request.user,
            'categories': Category.objects.all()
        })


def signin(request):
    if request.method == 'POST' and not request.user.is_authenticated:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # Valid login
        if user is not None:
            login(request, user)
            return index(request)
        # Invalid login
        else:
            return index(request)
        # If already authenticated just redirect to index
    elif request.user.is_authenticated:
        return index(request)
    else:
        form = SignInForm()
    return render(request, 'Sign_In.html', {
        'form': form
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Home')
    else:
        form = SignUpForm()
    return render(request, 'Sign_Up.html', {'form': form})


def logOut(request):
    if request.user.is_authenticated:
        logout(request)
    return index(request)


def about(request):
    return render(request, 'About.html', {
        'title': "About",
        'categories': Category.objects.all()

    })


def details(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'user/products/Details.html', {
        'product': product,
        'categories': Category.objects.all()
    })


def detailsmod(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'moderator/Details.html', {
        'product': product,
        'categories': Category.objects.all()
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
    return render(request, 'moderator/Update.html', {
        'form': form,
        'id': id,
        'categories': Category.objects.all()
    })


def delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('Home')


@login_required
def addtocart(request, id):
    product = Product.objects.get(pk=id)
    cartU = Cart.objects.get_or_create(user_id=request.user.id)[0]
    cartU.user = User.objects.get(pk=request.user.id)
    cartU.product.add(product)
    cartU.total += product.price
    cartU.save()
    return cart(request)


@login_required
def cart(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'user/products/Cart.html', {'products': cart.product, 'total': cart.total,
                                                       'categories': Category.objects.all()});


def revovetocart(request, id):
    product = Product.objects.get(pk=id)
    cart = Cart.objects.get(user=request.user)
    if cart.total > 0:
        cart.total = cart.total - product.price
    else:
        cart.total = 0.00
    cart.save()
    cart.product.remove(product)
    return render(request, 'user/products/Cart.html', {'products': cart.product, 'total': cart.total,
                                                       'categories': Category.objects.all()})


def filtercategory(request, id):
    queryset = Product.objects.all()
    queryset = queryset.filter(category_id=id)
    category = Category.objects.get(pk=id)
    return render(request, 'user/products/FilterCategories.html', {'category': category, 'products': queryset,
                                                                   'categories': Category.objects.all()});


def filter(searchText):
    return Product.objects.filter(
        Q(title__contains=searchText) |
        Q(description__contains=searchText)
    ).distinct()
