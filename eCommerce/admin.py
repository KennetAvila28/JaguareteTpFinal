from django.contrib import admin

from eCommerce.models import Category, Product, Cart
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
