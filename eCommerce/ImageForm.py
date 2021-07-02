from django import forms
from .models import Product


class ImageForm(forms.Form):
    # TODO: Form for upload image
    class Meta:
        model = Product
        fields = ('title', 'image')
