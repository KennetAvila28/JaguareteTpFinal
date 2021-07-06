from django import forms
from django.forms import ModelForm

from .models import Product
from .models import Category


class ProductForm(ModelForm):
    title = forms.CharField(max_length=50, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control-input'}),
                            label='Title ')
    description = forms.CharField(max_length=200, widget=forms.Textarea, label='Description ', required=True)
    category = forms.ModelChoiceField(Category.objects.all(), label='Category ')
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True, label='Price ')
    image = forms.ImageField(label='Image ')

    class Meta:
        model = Product
        fields = ['title', 'image', 'description', 'price', 'category']
