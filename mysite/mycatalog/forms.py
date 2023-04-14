from django import forms

from mycatalog.models import Product


class ProductImageForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    # class Meta:
    #     model = Product
    #     fields = 'content',


# class AddToCartForm(forms.Form):
#     quantity = forms.IntegerField(min_value=1, max_value=21, initial=1, label='')
#
#
# class ReviewForm(forms.Form):
#     review = forms.CharField(max_length='300', widget=forms.Textarea)