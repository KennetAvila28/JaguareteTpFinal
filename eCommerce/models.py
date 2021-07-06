from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description}'

    class Meta:
        ordering = ('description',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d/', blank=True)
    description = models.TextField(default='')
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}-{self.category}: ${self.price}'

    class Meta:
        ordering = ('title',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    count = models.PositiveIntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        return f'the user {self.user} have {self.count} items in the cart. the subtotal is ${self.subtotal}'
