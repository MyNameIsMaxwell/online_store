from django import forms

from mycatalog.models import Product


class ProductImageForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    # class Meta:
    #     model = Product
    #     fields = 'content',